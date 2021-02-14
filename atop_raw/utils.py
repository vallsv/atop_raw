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
