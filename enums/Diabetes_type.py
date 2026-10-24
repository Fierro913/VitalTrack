from enum import Enum
class DiabetesType(str,Enum):
    TYPE_1 : "tipo_1"
    TYPE_2 : "tipo_2"
    GESTACIONAL: "gestacional"
    OTRO: "otro"