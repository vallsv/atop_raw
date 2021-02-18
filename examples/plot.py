"""
Example of use of the library.
"""

import sys
import datetime
import argparse
import typing
from matplotlib import pyplot
import matplotlib.colors
import matplotlib.patches
from matplotlib.dates import YEARLY, DateFormatter, rrulewrapper, RRuleLocator

import atop_raw
from atop_raw.utils import ProcessReport


def normalize_str(data):
    if isinstance(data, bytes):
        return data.decode("ascii")
    return data


class ProcessMeasure(typing.NamedTuple):
    pid: int
    cmd: str
    name: str
    date: datetime.datetime
    cpu: float
    mem: float


class Data:
    def __init__(self):
        self.__stoage = {}
        self._count = 0

    def add(self, process: ProcessMeasure):
        if process.pid not in self.__stoage:
            self.__stoage[process.pid] = []
        self.__stoage[process.pid].append(process)
        self._count += 1

    def count(self):
        return self._count

    def list_pids(self):
        return list(self.__stoage.keys())

    def get_measures(self, pid):
        l = self.__stoage[pid]
        l = list(sorted(l, key=lambda p: p.date))
        return l


def draw(data: Data):
    available_colors = [c for c in matplotlib.colors.TABLEAU_COLORS]
    colors = {}
    print("PIDs found:")
    for pid in data.list_pids():
        l = data.get_measures(pid)
        m = l[0]
        if m.cmd not in colors:
            i = len(colors) % len(available_colors)
            c = available_colors[i]
            colors[m.cmd] = c
        print(f"- {m.pid} {colors[m.cmd]} {m.cmd}")

    cpu_ax = pyplot.subplot(2, 1, 1)
    cpu_ax.title.set_text("CPU in percent")
    cpu_ax.set_ylabel("cpu%")
    mem_ax = pyplot.subplot(2, 1, 2, sharex=cpu_ax)
    mem_ax.title.set_text("Memory in percent")
    mem_ax.set_ylabel("memory%")
    mem_ax.set_xlabel("datetime")

    # tick every 5th easter
    rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
    loc = RRuleLocator(rule)
    formatter = DateFormatter("%m/%d/%y")
    mem_ax.xaxis.set_major_locator(loc)
    mem_ax.xaxis.set_major_formatter(formatter)
    mem_ax.xaxis.set_tick_params(rotation=30, labelsize=10)
    cpu_ax.xaxis.set_visible(False)

    handles = []
    for pid in data.list_pids():
        l = data.get_measures(pid)
        cmd = l[0].cmd
        color = colors[cmd]
        handles.append(matplotlib.patches.Patch(color=color, label=pid))
        dates = [p.date for p in l]
        cpu = [p.cpu for p in l]
        mem = [p.mem for p in l]
        cpu_ax.plot_date(dates, cpu, linestyle="-", marker="", color=color, label=cmd)
        mem_ax.plot_date(dates, mem, linestyle="-", marker="", color=color, label=cmd)

    mem_ax.legend(handles=handles)
    pyplot.show()


def process(options):

    cmd_filters = options.cmd_filter[0].split(",")
    print(cmd_filters)

    data = Data()
    for filename in options.filenames:
        with open(filename, "rb") as stream:
            print(f"Extract {filename}")
            reader = atop_raw.create_reader(stream)

            for record in reader.records:
                print("-", record.curtime)
                # print(record.sstat)
                sstat = record.sstat
                report = ProcessReport(reader, sstat)

                for pstat in record.pstats:
                    cmd = normalize_str(pstat["gen"]["cmdline"])
                    for f in cmd_filters:
                        if f in cmd:
                            must_be_recorded = True
                            break
                    else:
                        must_be_recorded = False

                    if must_be_recorded:
                        name = normalize_str(pstat["gen"]["name"])
                        pid = pstat["gen"]["pid"]
                        mem = report.get_mem_percent(pstat)
                        cpu = report.get_cpu_percent(pstat)
                        process = ProcessMeasure(
                            pid=pid,
                            cmd=cmd,
                            name=name,
                            cpu=cpu,
                            mem=mem,
                            date=record.curtime,
                        )
                        data.add(process)
    return data


def main():
    parser = argparse.ArgumentParser(
        description="Process a set of atop files and plot the result."
    )
    parser.add_argument(
        "filenames", type=str, nargs="+", help="List of files to process"
    )
    parser.add_argument(
        "--cmd-filter",
        dest="cmd_filter",
        type=str,
        nargs=1,
        default=None,
        help="A list of regex separated by semi colon",
    )
    options = parser.parse_args(sys.argv[1:])

    data = process(options)
    draw(data)


if __name__ == "__main__":
    main()
