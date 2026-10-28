from enum import Enum


class IdType(str, Enum):
    CEDULA = "CEDULA"
    PASAPORTE = "PASAPORTE"
    NIT = "NIT"
    EXTRAJERIA = "EXTRAJERIA"