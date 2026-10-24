from enum import Enum
class Moment(str,Enum):
    AYUNAS : "ayunas"
    ANTES_COMIDA: "antes_comida"
    DESPUES_COMIDA: "despues_comida"
    ANTES_DORMIR: "antes_dormir"
    OTRO : "otro"
