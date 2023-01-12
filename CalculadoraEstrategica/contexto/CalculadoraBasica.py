from CalculadoraEstrategica.interfaces.BuilderCalculadora import BuilderCalculadora
from CalculadoraEstrategica.operaciones.Division import Division
from CalculadoraEstrategica.operaciones.Multiplicacion import Multiplicacion
from CalculadoraEstrategica.operaciones.Resta import Resta
from CalculadoraEstrategica.operaciones.Suma import Suma


class CalculadoraBasica:
    def __init__(self):
        self.operacion = None

    def is_operacion(self) -> bool:
        return self.operacion is not None

    def ejecuta_operacion(self, operando: float, operando2: float):
        return self.operacion.ejecuta(operando, operando2)


class CalculadoraBasicaBuilder(BuilderCalculadora):
    def __init__(self):
        self.calculadora = CalculadoraBasica()

    def operacion_por_usar(self, operador: str):

        if (operador == "+"):
            suma = Suma()
            self.calculadora.operacion = suma
        elif (operador == "-"):
            self.calculadora.operacion = Resta()
        elif (operador == "*"):
            self.calculadora.operacion = Multiplicacion()
        elif (operador == "/"):
            self.calculadora.operacion = Division()
        else:
            self.calculadora.operacion = None

        return self

    def build(self):
        return self.calculadora


class Director:
    def __init__(self, calculadora_builder: CalculadoraBasicaBuilder):
        self.cb = calculadora_builder

    def get_calculadora(self):
        return self.cb.operacion_por_usar("/").build()
