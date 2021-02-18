"""
Example of use of the library.

It parse a file read through all the content and display information on the fly.
"""

import sys
import atop_raw
from atop_raw.utils import ProcessReport


def normalize_str(data):
    if isinstance(data, bytes):
        return data.decode("ascii")
    return data


if len(sys.argv) == 1:
    raise RuntimeError("An atop file (at least) is expected")

filenames = sys.argv[1:]
for filename in filenames:
    with open(filename, "rb") as stream:
        print("=====================")
        print(f"{filename}")
        print("=====================")
        reader = atop_raw.create_reader(stream)
        print(reader.header)

        for record in reader.records:
            print()

            # print(record.header)
            # print(record.sstat)
            sstat = record.sstat
            report = ProcessReport(reader, sstat)

            for pstat in record.pstats:
                cmd = normalize_str(pstat["gen"]["cmdline"])
                name = normalize_str(pstat["gen"]["name"])
                pid = pstat["gen"]["pid"]
                mem = report.get_mem_percent(pstat)
                cpu = report.get_cpu_percent(pstat)
                if mem < 1:
                    continue
                if cpu < 1:
                    continue

                if cmd == "":
                    continue
                if len(cmd) > 70:
                    cmd = cmd[:70]
                print(
                    f"  {pid:>5} {name:<15} {cmd:<70}   mem:{mem: 5.1f}% cpu:{cpu: 5.1f}%"
                )
                # print(pstat)
            print()
            print(record.curtime)
        print()
