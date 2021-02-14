class ProcessReport:
    def __init__(self, reader, sstat):
        pagesize = reader.header["pagesize"]

        available_mem = sstat["mem"]["physmem"] * pagesize / 1024
        available_mem = max(available_mem, 1)
        self._available_mem = available_mem

        ss_cpu = sstat["cpu"]
        ss_cpu_all = sstat["cpu"]["all"]
        available_ticks = (
            ss_cpu_all["stime"]
            + ss_cpu_all["utime"]
            + ss_cpu_all["ntime"]
            + ss_cpu_all["itime"]
            + ss_cpu_all["wtime"]
            + ss_cpu_all["Itime"]
            + ss_cpu_all["Stime"]
            + ss_cpu_all["steal"]
            + ss_cpu_all["guest"]
        )
        available_ticks = available_ticks / ss_cpu["nrcpu"]
        available_ticks = max(available_ticks, 1)
        self._available_ticks = available_ticks

    def get_cpu_percent(self, pstat):
        """Compute the CPU load of a process as percent"""
        stime = pstat["cpu"]["stime"]
        utime = pstat["cpu"]["utime"]
        cpu = (stime + utime) * 100 / self._available_ticks
        return cpu

    def get_mem_percent(self, pstat):
        """Compute the memory usage of a process as percent"""
        rmem = pstat["mem"]["rmem"]
        mem = rmem * 100 / self._available_mem
        return mem

    def get_dsk_rw_sectors(self, pstat):
        """Compute the amount read/write sectors"""
        dsk = pstat["dsk"]["rsz"] + pstat["dsk"]["wsz"]
        return dsk

    def get_net_rw(self, pstat):
        """Compute the amount of up/down MB data exchanged in the network"""
        net = (
            pstat["net"]["tcpssz"]
            + pstat["net"]["tcprsz"]
            + pstat["net"]["udpssz"]
            + pstat["net"]["udprsz"]
        )
        return net / 1000000


class ProcessSet:
    """Helper to retrieve process statistics from pid, ppid, cmd..."""

    def __init__(self, pstats):
        self.__pstats = pstats
        self.__pid_to_index = {}
        self.__pid_to_child = {}
        self.__cmd_to_pid = {}
        self._parse()

    def _parse(self):
        states = set({})
        for i, pstat in enumerate(self.__pstats):
            pid = pstat["gen"]["pid"]
            ppid = pstat["gen"]["ppid"]
            cmd = pstat["gen"]["cmdline"].decode("ascii")
            self.__pid_to_index[pid] = i
            self.__cmd_to_pid[cmd] = pid
            if ppid not in self.__pid_to_child:
                self.__pid_to_child[ppid] = [pid]
            else:
                self.__pid_to_child[ppid].append(pid)

            state = chr(pstat["gen"]["state"])
            states.add(state)

    def pids_from_cmd(self, partial_cmd=None, states=None):
        for cmd, pid in self.__cmd_to_pid.items():
            if partial_cmd in cmd:
                yield pid

    def pids_from_parent_pid(self, ppid, recurive=True):
        pids = self.__pid_to_child.get(ppid)
        if pids is None:
            # No children
            return
        for pid in pids:
            yield pid
            if recurive:
                yield from self.pids_from_parent_pid(pid)

    def pstat(self, pid):
        i = self.__pid_to_index.get(pid)
        if i is None:
            return None
        return self.__pstats[i]

    def child_pstats(self, ppid, recursive=True):
        for pid in self.pids_from_parent_pid(ppid, recursive=recursive):
            yield self.pstat(pid)
