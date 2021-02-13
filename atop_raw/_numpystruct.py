import numpy
from pycstruct import pycstruct


_TYPE = {
    "int8": "i1",
    "uint8": "u1",
    "bool8": None,
    "int16": "i2",
    "uint16": "u2",
    "bool16": None,
    "float16": "f2",
    "int32": "i4",
    "uint32": "u4",
    "bool32": None,
    "float32": "f4",
    "int64": "i8",
    "uint64": "u8",
    "bool64": None,
    "float64": "f8",
}

_BYTEORDER = {
    "native": {"format": "="},
    "little": {"format": "<"},
    "big": {"format": ">"},
}


def to_dtype(struct) -> numpy.dtype:
    if isinstance(struct, pycstruct.BasicTypeDef):
        dtype = _TYPE[struct.type]
        if dtype is None:
            raise NotImplementedError(
                'Basic type "%s" is not implemented as dtype' % struct.type
            )
        byteorder = _BYTEORDER[struct.byteorder]["format"]
        dtype = byteorder + dtype
    elif isinstance(struct, pycstruct.StringDef):
        dtype = ("S", struct.length)
    elif isinstance(struct, pycstruct.StructDef):
        names = []
        formats = []
        offsets = []

        offset = 0
        for name, field in struct._StructDef__fields.items():
            datatype = field["type"]
            length = field["length"]

            if struct._StructDef__union:
                raise NotImplementedError("Union with dtype not implemented")

            if name.startswith("__pad"):
                pass
            else:
                if length > 1:
                    dtype = (to_dtype(datatype), length)
                else:
                    dtype = to_dtype(datatype)
                names.append(name)
                formats.append(dtype)
                offsets.append(offset)

            if not struct._StructDef__union:
                offset += datatype.size() * length

        dtype_def = {
            "names": names,
            "formats": formats,
            "offsets": offsets,
            "itemsize": struct.size(),
        }
        dtype = numpy.dtype(dtype_def)
    return dtype
