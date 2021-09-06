'''
Autor: Jesus Montes
Fecha: 16/junio/2021
'''
from numpy import float64
import pandas as pd 
def analisis_ramen(archivo:str)->dict():
    salida = {}
    df = pd.read_csv(archivo)
    filtroCup = df[df.Estilo == "Cup"]
    NotaCup = filtroCup["Nota"]
    sumNotaCup =0
    tamNotaCup = len(NotaCup)
    for i in NotaCup:
        sumNotaCup = sumNotaCup + i
        salida["promedio_cup"]= round(sumNotaCup/tamNotaCup,2)

    #FILTRO PACK, PROMEDIO PACK

    filtroPack = df[df.Estilo == "Pack"]
    filtroNotaPack = filtroPack["Nota"]
    sumNotaPack = 0
    tamNotaPack = len(filtroNotaPack)
    for p in filtroNotaPack:
        sumNotaPack = sumNotaPack + p
        salida["promedio_pack"]= round(sumNotaPack/tamNotaPack,2)

    #FILTRO Bowl, PROMEDIO Bowl
    filtroBowl = df[df.Estilo == "Bowl"]
    NotaBowl = filtroBowl["Nota"]
    sumNotaBowl = 0
    tamNotaBowl = len(NotaBowl)
    for b in NotaBowl:
        sumNotaBowl = sumNotaBowl + b
        salida["promedio_bowl"]= round(sumNotaBowl/tamNotaBowl,2)

    
    return salida
print(analisis_ramen("https://raw.githubusercontent.com/cardel/repositorios/main/mintic/p10/ramen-ratings_publico.csv"))