import io
import typing
import struct

MAGIC = b"\xef\xbe\xed\xfe"


class Version(typing.NamedTuple):
    flag: bool
    major: int
    minor: int


def _read_version(stream) -> Version:
    fmt = "<H"
    packer = struct.Struct(fmt)
    buffer = stream.read(packer.size)
    data = packer.unpack(buffer)[0]

    flag = data & 0x8000
    major = (data >> 8) & 0x7F
    minor = data & 0xFF
    return Version(flag, major, minor)


def create_reader(filename_or_stream):
    """
    Create a reader to allow to read the file as a stream.
    """
    if isinstance(filename_or_stream, str):
        filename = filename_or_stream
        stream = open(filename, "rb")
        return create_reader(stream)

    stream = filename_or_stream
    magic = stream.read(4)
    if magic != MAGIC:
        raise IOError("Not a atop raw data")
    v = _read_version(stream)
    if (v.major, v.minor) == (1, 26):
        from .atop_1_26 import Reader
    else:
        raise IOError(f"Unsupported atop file version {v.major}.{v.minor}")

    stream.seek(-6, io.SEEK_CUR)
    return Reader(stream)
