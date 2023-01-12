from abc import abstractmethod
from abc import ABCMeta


class Operacion(metaclass=ABCMeta):
    @abstractmethod
    def ejecuta(self, operando: float, operando2: float) -> float:
        pass
