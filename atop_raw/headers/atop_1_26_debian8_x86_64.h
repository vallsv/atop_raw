// This probably have to be tuned per systems

#pragma pack(8)
#define _UTSNAME_LENGTH 65
#define _UTSNAME_DOMAIN_LENGTH _UTSNAME_LENGTH
typedef unsigned long time_t;

// mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

struct utsname {
	// name of this implementation of the operating system
	char sysname[_UTSNAME_LENGTH];
	// name of this node within an implementation-defined
	// communications network
	char nodename[_UTSNAME_LENGTH];
	// current release level of this implementation
	char release[_UTSNAME_LENGTH];
	// current version level of this release
	char version[_UTSNAME_LENGTH];
	// name of the hardware type on which the system is running
	char machine[_UTSNAME_LENGTH];

#if _UTSNAME_DOMAIN_LENGTH - 0
    /* name of the domain of this node on the network.  */
    char domainname[_UTSNAME_DOMAIN_LENGTH];
#endif
};

struct rawheader {
	unsigned int magic;

	unsigned short aversion;    /* creator atop version with MSB */
	unsigned short future1; /* can be reused          */
	unsigned short future2; /* can be reused          */
	unsigned short rawheadlen; /* length of struct rawheader    */
	unsigned short rawreclen; /* length of struct rawrecord    */
	unsigned short hertz; /* clock interrupts per second   */
	unsigned short sfuture[6]; /* future use                    */
	unsigned int sstatlen; /* length of struct sstat        */
	unsigned int pstatlen; /* length of struct pstat        */
	struct utsname utsname; /* info about this system        */
	unsigned char cfuture[8]; /* future use                    */

	unsigned int pagesize; /* size of memory page (bytes)   */
	int supportflags; /* used features                 */
	int osrel; /* OS release number             */
	int osvers; /* OS version number             */
	int ossub; /* OS version subnumber          */
	int ifuture[6]; /* future use                    */
};

struct rawrecord {
	time_t curtime; /* current time (epoch)         */

	unsigned short flags; /* various flags                */
	unsigned short sfuture[3]; /* future use                   */

	unsigned int scomplen; /* length of compressed sstat   */
	unsigned int pcomplen; /* length of compressed pstat's */
	unsigned int interval; /* interval (number of seconds) */
	unsigned int nlist; /* number of processes in list  */
	unsigned int npresent; /* total number of processes    */
	unsigned int nexit; /* number of exited processes   */
	unsigned int ntrun; /* number of running  threads    */
	unsigned int ntslpi; /* number of sleeping threads(S)*/
	unsigned int ntslpu; /* number of sleeping threads(D)*/
	unsigned int nzombie; /* number of zombie processes   */
	unsigned int ifuture[6]; /* future use                   */
};

/************************************************************************/

#define    MAXCPU         64
#define    MAXDSK        256
#define    MAXLVM        256
#define    MAXMDD        128
#define    MAXDKNAM       32
#define    MAXINTF        32

typedef long long count_t;

struct ipv4_stats {
	count_t Forwarding;
	count_t DefaultTTL;
	count_t InReceives;
	count_t InHdrErrors;
	count_t InAddrErrors;
	count_t ForwDatagrams;
	count_t InUnknownProtos;
	count_t InDiscards;
	count_t InDelivers;
	count_t OutRequests;
	count_t OutDiscards;
	count_t OutNoRoutes;
	count_t ReasmTimeout;
	count_t ReasmReqds;
	count_t ReasmOKs;
	count_t ReasmFails;
	count_t FragOKs;
	count_t FragFails;
	count_t FragCreates;
};

struct icmpv4_stats {
	count_t InMsgs;
	count_t InErrors;
	count_t InDestUnreachs;
	count_t InTimeExcds;
	count_t InParmProbs;
	count_t InSrcQuenchs;
	count_t InRedirects;
	count_t InEchos;
	count_t InEchoReps;
	count_t InTimestamps;
	count_t InTimestampReps;
	count_t InAddrMasks;
	count_t InAddrMaskReps;
	count_t OutMsgs;
	count_t OutErrors;
	count_t OutDestUnreachs;
	count_t OutTimeExcds;
	count_t OutParmProbs;
	count_t OutSrcQuenchs;
	count_t OutRedirects;
	count_t OutEchos;
	count_t OutEchoReps;
	count_t OutTimestamps;
	count_t OutTimestampReps;
	count_t OutAddrMasks;
	count_t OutAddrMaskReps;
};

struct udpv4_stats {
	count_t InDatagrams;
	count_t NoPorts;
	count_t InErrors;
	count_t OutDatagrams;
};

struct tcp_stats {
	count_t RtoAlgorithm;
	count_t RtoMin;
	count_t RtoMax;
	count_t MaxConn;
	count_t ActiveOpens;
	count_t PassiveOpens;
	count_t AttemptFails;
	count_t EstabResets;
	count_t CurrEstab;
	count_t InSegs;
	count_t OutSegs;
	count_t RetransSegs;
	count_t InErrs;
	count_t OutRsts;
};

struct ipv6_stats {
	count_t Ip6InReceives;
	count_t Ip6InHdrErrors;
	count_t Ip6InTooBigErrors;
	count_t Ip6InNoRoutes;
	count_t Ip6InAddrErrors;
	count_t Ip6InUnknownProtos;
	count_t Ip6InTruncatedPkts;
	count_t Ip6InDiscards;
	count_t Ip6InDelivers;
	count_t Ip6OutForwDatagrams;
	count_t Ip6OutRequests;
	count_t Ip6OutDiscards;
	count_t Ip6OutNoRoutes;
	count_t Ip6ReasmTimeout;
	count_t Ip6ReasmReqds;
	count_t Ip6ReasmOKs;
	count_t Ip6ReasmFails;
	count_t Ip6FragOKs;
	count_t Ip6FragFails;
	count_t Ip6FragCreates;
	count_t Ip6InMcastPkts;
	count_t Ip6OutMcastPkts;
};

struct icmpv6_stats {
	count_t Icmp6InMsgs;
	count_t Icmp6InErrors;
	count_t Icmp6InDestUnreachs;
	count_t Icmp6InPktTooBigs;
	count_t Icmp6InTimeExcds;
	count_t Icmp6InParmProblems;
	count_t Icmp6InEchos;
	count_t Icmp6InEchoReplies;
	count_t Icmp6InGroupMembQueries;
	count_t Icmp6InGroupMembResponses;
	count_t Icmp6InGroupMembReductions;
	count_t Icmp6InRouterSolicits;
	count_t Icmp6InRouterAdvertisements;
	count_t Icmp6InNeighborSolicits;
	count_t Icmp6InNeighborAdvertisements;
	count_t Icmp6InRedirects;
	count_t Icmp6OutMsgs;
	count_t Icmp6OutDestUnreachs;
	count_t Icmp6OutPktTooBigs;
	count_t Icmp6OutTimeExcds;
	count_t Icmp6OutParmProblems;
	count_t Icmp6OutEchoReplies;
	count_t Icmp6OutRouterSolicits;
	count_t Icmp6OutNeighborSolicits;
	count_t Icmp6OutNeighborAdvertisements;
	count_t Icmp6OutRedirects;
	count_t Icmp6OutGroupMembResponses;
	count_t Icmp6OutGroupMembReductions;
};

struct udpv6_stats {
	count_t Udp6InDatagrams;
	count_t Udp6NoPorts;
	count_t Udp6InErrors;
	count_t Udp6OutDatagrams;
};

struct memstat {
	count_t physmem; /* number of physical pages     */
	count_t freemem; /* number of free     pages    */
	count_t buffermem; /* number of buffer   pages    */
	count_t slabmem; /* number of slab     pages    */
	count_t cachemem; /* number of cache    pages    */
	count_t cachedrt; /* number of cache    pages (dirty)    */

	count_t totswap; /* number of pages in swap    */
	count_t freeswap; /* number of free swap pages    */

	count_t pgscans; /* number of page scans        */
	count_t allocstall; /* try to free pages forced    */
	count_t swouts; /* number of pages swapped out    */
	count_t swins; /* number of pages swapped in    */

	count_t commitlim; /* commit limit in pages    */
	count_t committed; /* number of reserved pages    */
	count_t cfuture[4]; /* reserved for future use    */
};

struct netstat {
	struct ipv4_stats ipv4;
	struct icmpv4_stats icmpv4;
	struct udpv4_stats udpv4;

	struct ipv6_stats ipv6;
	struct icmpv6_stats icmpv6;
	struct udpv6_stats udpv6;

	struct tcp_stats tcp;
};

struct freqcnt {
	count_t maxfreq;/* frequency in MHz                    */
	count_t cnt; /* number of clock ticks times state   */
	count_t ticks; /* number of total clock ticks         */
	/* if zero, cnt is actul freq          */
};

struct percpu {
	int cpunr;
	signed char __manual_padding[4];
	count_t stime; /* system  time in clock ticks        */
	count_t utime; /* user    time in clock ticks        */
	count_t ntime; /* nice    time in clock ticks        */
	count_t itime; /* idle    time in clock ticks        */
	count_t wtime; /* iowait  time in clock ticks        */
	count_t Itime; /* irq     time in clock ticks        */
	count_t Stime; /* softirq time in clock ticks        */
	count_t steal; /* steal   time in clock ticks        */
	count_t guest; /* guest   time in clock ticks        */
	struct freqcnt freqcnt;/* frequency scaling info          */
	count_t cfuture[1]; /* reserved for future use    */

};

struct cpustat {
	count_t nrcpu; /* number of cpu's             */
	count_t devint; /* number of device interrupts         */
	count_t csw; /* number of context switches        */
	count_t nprocs; /* number of processes started          */
	float lavg1; /* load average last    minute          */
	float lavg5; /* load average last  5 minutes         */
	float lavg15; /* load average last 15 minutes         */
	count_t cfuture[4]; /* reserved for future use    */

	struct percpu all;
	struct percpu cpu[MAXCPU];
};

struct perdsk {
	char name[MAXDKNAM]; /* empty string for last        */
	count_t nread; /* number of read  transfers            */
	count_t nrsect; /* number of sectors read               */
	count_t nwrite; /* number of write transfers            */
	count_t nwsect; /* number of sectors written            */
	count_t io_ms; /* number of millisecs spent for I/O    */
	count_t avque; /* average queue length                 */
	count_t cfuture[4]; /* reserved for future use    */
};

struct dskstat {
	int ndsk; /* number of physical disks    */
	int nmdd; /* number of md volumes        */
	int nlvm; /* number of logical volumes    */
	struct perdsk dsk[MAXDSK];
	struct perdsk mdd[MAXMDD];
	struct perdsk lvm[MAXLVM];
};

struct perintf {
	char name[16]; /* empty string for last        */

	count_t rbyte; /* number of read bytes                 */
	count_t rpack; /* number of read packets               */
	count_t rerrs; /* receive errors                       */
	count_t rdrop; /* receive drops                        */
	count_t rfifo; /* receive fifo                         */
	count_t rframe; /* receive framing errors               */
	count_t rcompr; /* receive compressed                   */
	count_t rmultic;/* receive multicast                    */
	count_t rfuture[4]; /* reserved for future use    */

	count_t sbyte; /* number of written bytes              */
	count_t spack; /* number of written packets            */
	count_t serrs; /* transmit errors                      */
	count_t sdrop; /* transmit drops                       */
	count_t sfifo; /* transmit fifo                        */
	count_t scollis;/* collisions                           */
	count_t scarrier;/* transmit carrier                    */
	count_t scompr; /* transmit compressed                  */
	count_t sfuture[4]; /* reserved for future use    */

	long speed; /* interface speed in megabits/second    */
	char duplex; /* full duplex (boolean)         */
	count_t cfuture[4]; /* reserved for future use    */
};

struct intfstat {
	int nrintf;
	struct perintf intf[MAXINTF];
};

struct wwwstat {
	count_t accesses; /* total number of HTTP-requests    */
	count_t totkbytes; /* total kbytes transfer for HTTP-req   */
	count_t uptime; /* number of seconds since startup    */
	int bworkers; /* number of busy httpd-daemons        */
	int iworkers; /* number of idle httpd-daemons        */
};

struct sstat {
	struct cpustat cpu;
	struct memstat mem;
	struct netstat net;
	struct intfstat intf;
	struct dskstat dsk;

	struct wwwstat www;
};

#define	PNAMLEN		15
#define	CMDLEN		150

/*
 ** structure containing only relevant process-info extracted
 ** from kernel's process-administration
 */
struct pstat {
	/* GENERAL PROCESS INFO 					*/
	struct gen {
		int	pid;		/* process identification 	*/
		int	ppid;           /* parent process identification*/
		int	ruid;		/* real  user  identification 	*/
		int	euid;		/* eff.  user  identification 	*/
		int	suid;		/* saved user  identification 	*/
		int	fsuid;		/* fs    user  identification 	*/
		int	rgid;		/* real  group identification 	*/
		int	egid;		/* eff.  group identification 	*/
		int	sgid;		/* saved group identification 	*/
		int	fsgid;		/* fs    group identification 	*/
		int	nthr;		/* number of threads in tgroup 	*/
		char	name[PNAMLEN+1];/* process name string       	*/
		char 	state;		/* process state ('E' = exited)	*/
		int	excode;		/* process exit status		*/
		time_t 	btime;		/* process start time (epoch)	*/
		time_t 	elaps;		/* process elaps time (hertz)	*/
		char	cmdline[CMDLEN+1];/* command-line string       	*/
		int	nthrslpi;	/* # threads in state 'S'       */
		int	nthrslpu;	/* # threads in state 'D'       */
		int	nthrrun;	/* # threads in state 'R'       */
		int	ifuture[1];     /* reserved                     */
	} gen;

	/* CPU STATISTICS						*/
	struct cpu {
		count_t	utime;		/* time user   text (ticks) 	*/
		count_t	stime;		/* time system text (ticks) 	*/
		int	nice;		/* nice value                   */
		int	prio;		/* priority                     */
		int	rtprio;		/* realtime priority            */
		int	policy;		/* scheduling policy            */
		int	curcpu;		/* current processor            */
		int	sleepavg;       /* sleep average percentage     */
		int	ifuture[4];	/* reserved for future use	*/
		count_t	cfuture[4];	/* reserved for future use	*/
	} cpu;

	/* DISK STATISTICS						*/
	struct dsk {
		count_t	rio;		/* number of read requests 	*/
		count_t	rsz;		/* cumulative # sectors read	*/
		count_t	wio;		/* number of write requests 	*/
		count_t	wsz;		/* cumulative # sectors written	*/
		count_t	cwsz;		/* cumulative # written sectors */
					/* being cancelled              */
		count_t	cfuture[4];	/* reserved for future use	*/
	} dsk;

	/* MEMORY STATISTICS						*/
	struct mem {
		count_t	minflt;		/* number of page-reclaims 	*/
		count_t	majflt;		/* number of page-faults 	*/
		count_t	shtext;		/* text     memory (Kb)         */
		count_t	vmem;		/* virtual  memory (Kb)		*/
		count_t	rmem;		/* resident memory (Kb)		*/
		count_t vgrow;		/* virtual  growth (Kb)    	*/
		count_t rgrow;		/* resident growth (Kb)     	*/
		count_t	cfuture[4];	/* reserved for future use	*/
	} mem;

	/* NETWORK STATISTICS						*/
	struct net {
		count_t tcpsnd;		/* number of TCP-packets sent	*/
		count_t tcpssz;		/* cumulative size packets sent	*/
		count_t	tcprcv;		/* number of TCP-packets recved	*/
		count_t tcprsz;		/* cumulative size packets rcvd	*/
		count_t	udpsnd;		/* number of UDP-packets sent	*/
		count_t udpssz;		/* cumulative size packets sent	*/
		count_t	udprcv;		/* number of UDP-packets recved	*/
		count_t udprsz;		/* cumulative size packets sent	*/
		count_t	rawsnd;		/* number of raw packets sent	*/
		count_t	rawrcv;		/* number of raw packets recved	*/
		count_t	cfuture[4];	/* reserved for future use	*/
	} net;
};
