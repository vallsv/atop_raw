
"""
Autogenerated file from atop_1_26_debian8_x86_64.h
using pycstruct and castxml
"""


class Struct:
    def __init__(self, dtype, size):
        self._dtype = dtype
        self._size = size

    def dtype(self):
        return self._dtype

    def size(self):
        return self._size


dtype = {
    "names": [
        "magic",
        "aversion",
        "future1",
        "future2",
        "rawheadlen",
        "rawreclen",
        "hertz",
        "sfuture",
        "sstatlen",
        "pstatlen",
        "utsname",
        "cfuture",
        "pagesize",
        "supportflags",
        "osrel",
        "osvers",
        "ossub",
        "ifuture",
    ],
    "formats": [
        "=u4",
        "=u2",
        "=u2",
        "=u2",
        "=u2",
        "=u2",
        "=u2",
        ("=u2", 6),
        "=u4",
        "=u4",
        {
            "names": [
                "sysname",
                "nodename",
                "release",
                "version",
                "machine",
                "domainname",
            ],
            "formats": [
                ("S", 65),
                ("S", 65),
                ("S", 65),
                ("S", 65),
                ("S", 65),
                ("S", 65),
            ],
            "offsets": [0, 65, 130, 195, 260, 325],
            "itemsize": 390,
        },
        ("=u1", 8),
        "=u4",
        "=i4",
        "=i4",
        "=i4",
        "=i4",
        ("=i4", 6),
    ],
    "offsets": [
        0,
        4,
        6,
        8,
        10,
        12,
        14,
        16,
        28,
        32,
        36,
        426,
        436,
        440,
        444,
        448,
        452,
        456,
    ],
    "itemsize": 480,
}
size = 480
rawheader_t = Struct(dtype, size)

dtype = {
    "names": [
        "curtime",
        "flags",
        "sfuture",
        "scomplen",
        "pcomplen",
        "interval",
        "nlist",
        "npresent",
        "nexit",
        "ntrun",
        "ntslpi",
        "ntslpu",
        "nzombie",
        "ifuture",
    ],
    "formats": [
        "=u8",
        "=u2",
        ("=u2", 3),
        "=u4",
        "=u4",
        "=u4",
        "=u4",
        "=u4",
        "=u4",
        "=u4",
        "=u4",
        "=u4",
        "=u4",
        ("=u4", 6),
    ],
    "offsets": [0, 8, 10, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56],
    "itemsize": 80,
}
size = 80
rawrecord_t = Struct(dtype, size)

dtype = {
    "names": ["cpu", "mem", "net", "intf", "dsk", "www"],
    "formats": [
        {
            "names": [
                "nrcpu",
                "devint",
                "csw",
                "nprocs",
                "lavg1",
                "lavg5",
                "lavg15",
                "cfuture",
                "all",
                "cpu",
            ],
            "formats": [
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=f4",
                "=f4",
                "=f4",
                ("=i8", 4),
                {
                    "names": [
                        "cpunr",
                        "__manual_padding",
                        "stime",
                        "utime",
                        "ntime",
                        "itime",
                        "wtime",
                        "Itime",
                        "Stime",
                        "steal",
                        "guest",
                        "freqcnt",
                        "cfuture",
                    ],
                    "formats": [
                        "=i4",
                        ("=i1", 4),
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        {
                            "names": ["maxfreq", "cnt", "ticks"],
                            "formats": ["=i8", "=i8", "=i8"],
                            "offsets": [0, 8, 16],
                            "itemsize": 24,
                        },
                        "=i8",
                    ],
                    "offsets": [0, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 104],
                    "itemsize": 112,
                },
                (
                    {
                        "names": [
                            "cpunr",
                            "__manual_padding",
                            "stime",
                            "utime",
                            "ntime",
                            "itime",
                            "wtime",
                            "Itime",
                            "Stime",
                            "steal",
                            "guest",
                            "freqcnt",
                            "cfuture",
                        ],
                        "formats": [
                            "=i4",
                            ("=i1", 4),
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            {
                                "names": ["maxfreq", "cnt", "ticks"],
                                "formats": ["=i8", "=i8", "=i8"],
                                "offsets": [0, 8, 16],
                                "itemsize": 24,
                            },
                            "=i8",
                        ],
                        "offsets": [0, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 104],
                        "itemsize": 112,
                    },
                    64,
                ),
            ],
            "offsets": [0, 8, 16, 24, 32, 36, 40, 48, 80, 192],
            "itemsize": 7360,
        },
        {
            "names": [
                "physmem",
                "freemem",
                "buffermem",
                "slabmem",
                "cachemem",
                "cachedrt",
                "totswap",
                "freeswap",
                "pgscans",
                "allocstall",
                "swouts",
                "swins",
                "commitlim",
                "committed",
                "cfuture",
            ],
            "formats": [
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                ("=i8", 4),
            ],
            "offsets": [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112],
            "itemsize": 144,
        },
        {
            "names": ["ipv4", "icmpv4", "udpv4", "ipv6", "icmpv6", "udpv6", "tcp"],
            "formats": [
                {
                    "names": [
                        "Forwarding",
                        "DefaultTTL",
                        "InReceives",
                        "InHdrErrors",
                        "InAddrErrors",
                        "ForwDatagrams",
                        "InUnknownProtos",
                        "InDiscards",
                        "InDelivers",
                        "OutRequests",
                        "OutDiscards",
                        "OutNoRoutes",
                        "ReasmTimeout",
                        "ReasmReqds",
                        "ReasmOKs",
                        "ReasmFails",
                        "FragOKs",
                        "FragFails",
                        "FragCreates",
                    ],
                    "formats": [
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                    ],
                    "offsets": [
                        0,
                        8,
                        16,
                        24,
                        32,
                        40,
                        48,
                        56,
                        64,
                        72,
                        80,
                        88,
                        96,
                        104,
                        112,
                        120,
                        128,
                        136,
                        144,
                    ],
                    "itemsize": 152,
                },
                {
                    "names": [
                        "InMsgs",
                        "InErrors",
                        "InDestUnreachs",
                        "InTimeExcds",
                        "InParmProbs",
                        "InSrcQuenchs",
                        "InRedirects",
                        "InEchos",
                        "InEchoReps",
                        "InTimestamps",
                        "InTimestampReps",
                        "InAddrMasks",
                        "InAddrMaskReps",
                        "OutMsgs",
                        "OutErrors",
                        "OutDestUnreachs",
                        "OutTimeExcds",
                        "OutParmProbs",
                        "OutSrcQuenchs",
                        "OutRedirects",
                        "OutEchos",
                        "OutEchoReps",
                        "OutTimestamps",
                        "OutTimestampReps",
                        "OutAddrMasks",
                        "OutAddrMaskReps",
                    ],
                    "formats": [
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                    ],
                    "offsets": [
                        0,
                        8,
                        16,
                        24,
                        32,
                        40,
                        48,
                        56,
                        64,
                        72,
                        80,
                        88,
                        96,
                        104,
                        112,
                        120,
                        128,
                        136,
                        144,
                        152,
                        160,
                        168,
                        176,
                        184,
                        192,
                        200,
                    ],
                    "itemsize": 208,
                },
                {
                    "names": ["InDatagrams", "NoPorts", "InErrors", "OutDatagrams"],
                    "formats": ["=i8", "=i8", "=i8", "=i8"],
                    "offsets": [0, 8, 16, 24],
                    "itemsize": 32,
                },
                {
                    "names": [
                        "Ip6InReceives",
                        "Ip6InHdrErrors",
                        "Ip6InTooBigErrors",
                        "Ip6InNoRoutes",
                        "Ip6InAddrErrors",
                        "Ip6InUnknownProtos",
                        "Ip6InTruncatedPkts",
                        "Ip6InDiscards",
                        "Ip6InDelivers",
                        "Ip6OutForwDatagrams",
                        "Ip6OutRequests",
                        "Ip6OutDiscards",
                        "Ip6OutNoRoutes",
                        "Ip6ReasmTimeout",
                        "Ip6ReasmReqds",
                        "Ip6ReasmOKs",
                        "Ip6ReasmFails",
                        "Ip6FragOKs",
                        "Ip6FragFails",
                        "Ip6FragCreates",
                        "Ip6InMcastPkts",
                        "Ip6OutMcastPkts",
                    ],
                    "formats": [
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                    ],
                    "offsets": [
                        0,
                        8,
                        16,
                        24,
                        32,
                        40,
                        48,
                        56,
                        64,
                        72,
                        80,
                        88,
                        96,
                        104,
                        112,
                        120,
                        128,
                        136,
                        144,
                        152,
                        160,
                        168,
                    ],
                    "itemsize": 176,
                },
                {
                    "names": [
                        "Icmp6InMsgs",
                        "Icmp6InErrors",
                        "Icmp6InDestUnreachs",
                        "Icmp6InPktTooBigs",
                        "Icmp6InTimeExcds",
                        "Icmp6InParmProblems",
                        "Icmp6InEchos",
                        "Icmp6InEchoReplies",
                        "Icmp6InGroupMembQueries",
                        "Icmp6InGroupMembResponses",
                        "Icmp6InGroupMembReductions",
                        "Icmp6InRouterSolicits",
                        "Icmp6InRouterAdvertisements",
                        "Icmp6InNeighborSolicits",
                        "Icmp6InNeighborAdvertisements",
                        "Icmp6InRedirects",
                        "Icmp6OutMsgs",
                        "Icmp6OutDestUnreachs",
                        "Icmp6OutPktTooBigs",
                        "Icmp6OutTimeExcds",
                        "Icmp6OutParmProblems",
                        "Icmp6OutEchoReplies",
                        "Icmp6OutRouterSolicits",
                        "Icmp6OutNeighborSolicits",
                        "Icmp6OutNeighborAdvertisements",
                        "Icmp6OutRedirects",
                        "Icmp6OutGroupMembResponses",
                        "Icmp6OutGroupMembReductions",
                    ],
                    "formats": [
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                    ],
                    "offsets": [
                        0,
                        8,
                        16,
                        24,
                        32,
                        40,
                        48,
                        56,
                        64,
                        72,
                        80,
                        88,
                        96,
                        104,
                        112,
                        120,
                        128,
                        136,
                        144,
                        152,
                        160,
                        168,
                        176,
                        184,
                        192,
                        200,
                        208,
                        216,
                    ],
                    "itemsize": 224,
                },
                {
                    "names": [
                        "Udp6InDatagrams",
                        "Udp6NoPorts",
                        "Udp6InErrors",
                        "Udp6OutDatagrams",
                    ],
                    "formats": ["=i8", "=i8", "=i8", "=i8"],
                    "offsets": [0, 8, 16, 24],
                    "itemsize": 32,
                },
                {
                    "names": [
                        "RtoAlgorithm",
                        "RtoMin",
                        "RtoMax",
                        "MaxConn",
                        "ActiveOpens",
                        "PassiveOpens",
                        "AttemptFails",
                        "EstabResets",
                        "CurrEstab",
                        "InSegs",
                        "OutSegs",
                        "RetransSegs",
                        "InErrs",
                        "OutRsts",
                    ],
                    "formats": [
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                        "=i8",
                    ],
                    "offsets": [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104],
                    "itemsize": 112,
                },
            ],
            "offsets": [0, 152, 360, 392, 568, 792, 824],
            "itemsize": 936,
        },
        {
            "names": ["nrintf", "intf"],
            "formats": [
                "=i4",
                (
                    {
                        "names": [
                            "name",
                            "rbyte",
                            "rpack",
                            "rerrs",
                            "rdrop",
                            "rfifo",
                            "rframe",
                            "rcompr",
                            "rmultic",
                            "rfuture",
                            "sbyte",
                            "spack",
                            "serrs",
                            "sdrop",
                            "sfifo",
                            "scollis",
                            "scarrier",
                            "scompr",
                            "sfuture",
                            "speed",
                            "duplex",
                            "cfuture",
                        ],
                        "formats": [
                            ("S", 16),
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            ("=i8", 4),
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            ("=i8", 4),
                            "=i8",
                            "=i1",
                            ("=i8", 4),
                        ],
                        "offsets": [
                            0,
                            16,
                            24,
                            32,
                            40,
                            48,
                            56,
                            64,
                            72,
                            80,
                            112,
                            120,
                            128,
                            136,
                            144,
                            152,
                            160,
                            168,
                            176,
                            208,
                            216,
                            224,
                        ],
                        "itemsize": 256,
                    },
                    32,
                ),
            ],
            "offsets": [0, 8],
            "itemsize": 8200,
        },
        {
            "names": ["ndsk", "nmdd", "nlvm", "dsk", "mdd", "lvm"],
            "formats": [
                "=i4",
                "=i4",
                "=i4",
                (
                    {
                        "names": [
                            "name",
                            "nread",
                            "nrsect",
                            "nwrite",
                            "nwsect",
                            "io_ms",
                            "avque",
                            "cfuture",
                        ],
                        "formats": [
                            ("S", 32),
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            ("=i8", 4),
                        ],
                        "offsets": [0, 32, 40, 48, 56, 64, 72, 80],
                        "itemsize": 112,
                    },
                    256,
                ),
                (
                    {
                        "names": [
                            "name",
                            "nread",
                            "nrsect",
                            "nwrite",
                            "nwsect",
                            "io_ms",
                            "avque",
                            "cfuture",
                        ],
                        "formats": [
                            ("S", 32),
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            ("=i8", 4),
                        ],
                        "offsets": [0, 32, 40, 48, 56, 64, 72, 80],
                        "itemsize": 112,
                    },
                    128,
                ),
                (
                    {
                        "names": [
                            "name",
                            "nread",
                            "nrsect",
                            "nwrite",
                            "nwsect",
                            "io_ms",
                            "avque",
                            "cfuture",
                        ],
                        "formats": [
                            ("S", 32),
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            "=i8",
                            ("=i8", 4),
                        ],
                        "offsets": [0, 32, 40, 48, 56, 64, 72, 80],
                        "itemsize": 112,
                    },
                    256,
                ),
            ],
            "offsets": [0, 4, 8, 16, 28688, 43024],
            "itemsize": 71696,
        },
        {
            "names": ["accesses", "totkbytes", "uptime", "bworkers", "iworkers"],
            "formats": ["=i8", "=i8", "=i8", "=i4", "=i4"],
            "offsets": [0, 8, 16, 24, 28],
            "itemsize": 32,
        },
    ],
    "offsets": [0, 7360, 7504, 8440, 16640, 88336],
    "itemsize": 88368,
}
size = 88368
sstat_t = Struct(dtype, size)

dtype = {
    "names": ["gen", "cpu", "dsk", "mem", "net"],
    "formats": [
        {
            "names": [
                "pid",
                "ppid",
                "ruid",
                "euid",
                "suid",
                "fsuid",
                "rgid",
                "egid",
                "sgid",
                "fsgid",
                "nthr",
                "name",
                "state",
                "excode",
                "btime",
                "elaps",
                "cmdline",
                "nthrslpi",
                "nthrslpu",
                "nthrrun",
                "ifuture",
            ],
            "formats": [
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                ("S", 16),
                "=i1",
                "=i4",
                "=u8",
                "=u8",
                ("S", 151),
                "=i4",
                "=i4",
                "=i4",
                "=i4",
            ],
            "offsets": [
                0,
                4,
                8,
                12,
                16,
                20,
                24,
                28,
                32,
                36,
                40,
                44,
                60,
                64,
                72,
                80,
                88,
                240,
                244,
                248,
                252,
            ],
            "itemsize": 256,
        },
        {
            "names": [
                "utime",
                "stime",
                "nice",
                "prio",
                "rtprio",
                "policy",
                "curcpu",
                "sleepavg",
                "ifuture",
                "cfuture",
            ],
            "formats": [
                "=i8",
                "=i8",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                "=i4",
                ("=i4", 4),
                ("=i8", 4),
            ],
            "offsets": [0, 8, 16, 20, 24, 28, 32, 36, 40, 56],
            "itemsize": 88,
        },
        {
            "names": ["rio", "rsz", "wio", "wsz", "cwsz", "cfuture"],
            "formats": ["=i8", "=i8", "=i8", "=i8", "=i8", ("=i8", 4)],
            "offsets": [0, 8, 16, 24, 32, 40],
            "itemsize": 72,
        },
        {
            "names": [
                "minflt",
                "majflt",
                "shtext",
                "vmem",
                "rmem",
                "vgrow",
                "rgrow",
                "cfuture",
            ],
            "formats": ["=i8", "=i8", "=i8", "=i8", "=i8", "=i8", "=i8", ("=i8", 4)],
            "offsets": [0, 8, 16, 24, 32, 40, 48, 56],
            "itemsize": 88,
        },
        {
            "names": [
                "tcpsnd",
                "tcpssz",
                "tcprcv",
                "tcprsz",
                "udpsnd",
                "udpssz",
                "udprcv",
                "udprsz",
                "rawsnd",
                "rawrcv",
                "cfuture",
            ],
            "formats": [
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                "=i8",
                ("=i8", 4),
            ],
            "offsets": [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80],
            "itemsize": 112,
        },
    ],
    "offsets": [0, 256, 344, 416, 504],
    "itemsize": 616,
}
size = 616
pstat_t = Struct(dtype, size)