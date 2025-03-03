from fastapi import FastAPI

from CalculadoraEstrategica.contexto.CalculadoraBasica import CalculadoraBasica
from CalculadoraEstrategica.interfaces.Operacion import Operacion

app = FastAPI(title='CalculadoraAPI',
              description='Esta es una prueba',
              version='1.0.1')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api/calculadorabasica/operacion/")
async def calcula(num: int = 0 , num2: int = 0):
    resultado = 0
    calculadora: CalculadoraBasica = CalculadoraBasica.Builder.operacion(self=Builder, operador="+").build()
    if calculadora.is_operacion():
        resultado = calculadora.ejecuta_operacion(num, num2)
        return {"resultado": resultado}
