from CalculadoraEstrategica.interfaces.Operacion import Operacion


class Multiplicacion(Operacion):
    def ejecuta(self, operando: float, operando2: float) -> float:
        return operando * operando2