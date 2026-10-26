from enum import Enum, auto
class IdType(str, Enum):
    CEDULA = "CEDULA"
    PASAPORTE = "PASAPORTE"
    NIT = "NIT"
    EXTRAJERIA = "EXTRAJERIA"
