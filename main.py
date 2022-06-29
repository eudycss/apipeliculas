#Edwin Cabascango - Aplicaciones Moviles

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from modelo import *
import database as bd

app = FastAPI()

@app.get('/')

def Inicio():
    return {"Mensaje ": "Bienvenido Sepas API Crud peliculas"}

@app.post("/Peliculas/Agregar", tags=['Peliculas'])
def Agregar (P:Peliculas):
    bd.GuardarPeliculas(P)
    return {"Mensaje":"Los datos fueron Guardados."}

@app.get("/Peliculas/lista", tags=['Peliculas'])

def Lista_de_Peliculas():
    Peliculas = bd.CargarPeliculas()
    return Peliculas

@app.put("/Peliculas/Actualizar",tags=['Peliculas'])

def Actualizar(P:Peliculas):
    bd.ActualizarPeliculas(P)
    return  {"Mensaje":"Los datos fueron actualizados."}

@app.delete("/Peliculas/Eliminar",tags=['Peliculas'])

def Eliminar(P:Peliculas):
    bd.EliminarPeliculas(P)
    return  {"Mensaje":"La película fue eliminada."}
