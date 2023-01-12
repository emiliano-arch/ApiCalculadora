from CalculadoraEstrategica.interfaces.BuilderCalculadora import BuilderCalculadora
from CalculadoraEstrategica.operaciones.Division import Division
from CalculadoraEstrategica.operaciones.Multiplicacion import Multiplicacion
from CalculadoraEstrategica.operaciones.Resta import Resta
from CalculadoraEstrategica.operaciones.Suma import Suma


class CalculadoraBasica:
    def __init__(self):
        self._operacion = None

    def is_operacion(self) -> bool:
        return self._operacion is not None

    def ejecuta_operacion(self, operando: float, operando2: float):
        return self._operacion.ejecuta(operando, operando2)

    class Builder(BuilderCalculadora):
        # calculadora: CalculadoraBasica = Non

        def __init__(self):
            self._calculadora: CalculadoraBasica = CalculadoraBasica()

        @staticmethod
        def operacion(operador: str, self) -> BuilderCalculadora:
            match operador:
                case "+":
                    self._calculadora.operacion = Suma()
                case "-":
                    self._calculadora.operacion = Resta()
                case "*":
                    self._calculadora.operacion = Multiplicacion()
                case "x":
                    self._calculadora.operacion = Division()
                case _:
                    self._calculadora.operacion = None
            return self

        @staticmethod
        def build(self):
            return self._calculadora
