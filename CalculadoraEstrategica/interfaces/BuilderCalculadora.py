from abc import abstractmethod
from abc import ABCMeta


class BuilderCalculadora(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def operacion(self, operador: str):
        pass


