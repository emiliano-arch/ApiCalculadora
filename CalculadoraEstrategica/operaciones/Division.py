from CalculadoraEstrategica.interfaces.Operacion import Operacion


class Division(Operacion):
    def ejecuta(self, operando: float, operando2: float) -> float:
        return operando / operando2