"""
The `atop` 1.26 file format depend on C structure which can
differ between atop builds.

As result this file have to be tuned to work.
"""

from __future__ import annotations
import io
import zlib
import typing
import logging
import datetime
import numpy
import os.path

_logger = logging.getLogger(__name__)


try:
    import pycstruct

    _PATH = os.path.dirname(__file__)
    FILE_DESCRIPTION = os.path.join(_PATH, "headers", "atop_1_26_debian8_x86_64.h")
    c_structs = pycstruct.parse_file(FILE_DESCRIPTION)

    rawheader_t = c_structs["rawheader"]
    rawrecord_t = c_structs["rawrecord"]
    sstat_t = c_structs["sstat"]
    pstat_t = c_structs["pstat"]
except Exception:
    from .headers import atop_1_26_debian8_x86_64 as headers

    rawheader_t = headers.rawheader_t
    rawrecord_t = headers.rawrecord_t
    sstat_t = headers.sstat_t
    pstat_t = headers.pstat_t


class NoMoreRecord(IOError):
    pass


def info(rawheader):
    headers = [
        ("rawheadlen", "rawheader"),
        ("rawreclen", "rawrecord"),
        ("sstatlen", "sstat"),
        ("pstatlen", "pstat"),
    ]

    print("HEADER SANITY")
    print("-------------")
    print("Name            Def     File Status")
    print(f"---------- -------- -------- ------")
    for nsize, n in headers:
        in_file = rawheader[nsize]
        in_description = c_structs[n].size()
        ok = "OK" if in_file == in_description else "ERROR"
        print(f"{n:<10} {in_description:>8} {in_file:>8} {ok:<6}")
    print("")
    print("If this values does not match, the definition have to be reworked manually")


class Record:
    def __init__(self, reader: Reader, pos_in_file):
        self._pos_in_file = pos_in_file
        self._reader = reader
        self._header = self._reader.read_record_header()
        if self._header is None:
            raise NoMoreRecord

    @property
    def curtime(self) -> datetime.datetime:
        """Returns a datetime object for the curtime"""
        curtime = self._header["curtime"]
        d = datetime.datetime.fromtimestamp(curtime)
        return d

    def pos_in_file(self):
        return self._pos_in_file

    @property
    def header(self) -> rawrecord_t:
        return self._header

    @property
    def sstat(self) -> sstat_t:
        reader = self._reader
        reader.move_to_sstat(self)
        sstat = reader.read_sstat(self)
        return sstat

    @property
    def pstats(self) -> typing.List[pstat_t]:
        reader = self._reader
        reader.move_to_pstats(self)
        sstat = reader.read_pstats(self)
        return sstat


class Reader:
    """Reader for atop file version 1.26.

    It only stores header blocks. The content is read and decompressed on
    depend.

    It can be used to read the file sequencially, or in random mode if you
    stores each records. This will read again the file at right place to read
    the statistics.

    Argument
        stream: stream at start of of a atop file

    Raises
        IOError
    """

    def __init__(self, stream):
        self._stream = stream
        self._init()

    def _init(self):
        rawheader = self.read_header()
        self._rawheader = rawheader

        if rawheader["rawheadlen"] < rawheader_t.size():
            raise IOError(
                "Read rawheader size smaller than expected: This is machine dependent. The definition have to be manualy fixed"
            )
        if rawheader["rawreclen"] < rawrecord_t.size():
            raise IOError(
                "Read rawrecord size smaller than expected: This is machine dependent. The definition have to be manualy fixed"
            )

        if rawheader["sstatlen"] < sstat_t.size():
            raise IOError(
                "Read sstat size smaller than expected: This is machine dependent. The definition have to be manualy fixed"
            )

        if rawheader["pstatlen"] < pstat_t.size():
            raise IOError(
                "Read pstat size smaller than expected: This is machine dependent. The definition have to be manualy fixed"
            )

    @property
    def header(self) -> rawheader_t:
        """Returns the file header"""
        return self._rawheader

    @property
    def records(self) -> typing.List[Record]:
        """List all the records available in the file"""
        record = None
        while True:
            if record is not None:
                # setup the right place to rea the next record
                self.move_to_next_record(record)
            pos = self._stream.tell()
            try:
                record = Record(self, pos)
            except NoMoreRecord:
                break
            yield record

    def read_header(self) -> rawheader_t:
        """Read a rawheader_t from the current position of the stream"""
        data = self._stream.read(rawheader_t.size())
        rawheader = numpy.frombuffer(data, dtype=rawheader_t.dtype())[0]
        return rawheader

    def read_record_header(self) -> typing.Optional[rawrecord_t]:
        """Read a rawrecord_t from the current position of the stream"""
        data = self._stream.read(rawrecord_t.size())
        if data == b"":
            return None
        rawrecord = numpy.frombuffer(data, dtype=rawrecord_t.dtype())[0]
        return rawrecord

    def read_sstat(self, record: Record) -> sstat_t:
        """Read a sstat_t from the current position of the stream"""
        size = record.header["scomplen"]
        compressed_sstat = self._stream.read(size)
        sstat = zlib.decompress(compressed_sstat)
        assert len(sstat) == sstat_t.size()
        sstat = numpy.frombuffer(sstat, dtype=sstat_t.dtype(), count=1)[0]
        return sstat

    def read_pstats(self, record: Record) -> typing.List[pstat_t]:
        """Read a list of pstat_t from the current position of the stream"""
        size = record.header["pcomplen"]
        compressed_pstat = self._stream.read(size)
        npresent = record.header["npresent"]
        pstat = zlib.decompress(compressed_pstat)
        pstats = numpy.frombuffer(pstat, dtype=pstat_t.dtype(), count=npresent)
        return pstats

    def move_to_next_record(self, record: Record):
        sstat_length = record.header["scomplen"]
        pstat_length = record.header["pcomplen"]
        pos = record.pos_in_file() + rawrecord_t.size() + sstat_length + pstat_length
        self._stream.seek(pos, io.SEEK_SET)

    def move_to_sstat(self, record: Record):
        pos = record.pos_in_file() + rawrecord_t.size()
        self._stream.seek(pos, io.SEEK_SET)

    def move_to_pstats(self, record: Record):
        sstat_length = record.header["scomplen"]
        pos = record.pos_in_file() + rawrecord_t.size() + sstat_length
        self._stream.seek(pos, io.SEEK_SET)
