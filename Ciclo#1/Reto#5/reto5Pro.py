import pandas as pd
def analisis_ramen(archivo:str)->dict():
  datos = pd.read_csv(archivo)

  datos_cup = datos[datos["Estilo"]=="Cup"]
  datos_pack= datos[datos["Estilo"]=="Pack"]
  datos_bowl = datos[datos["Estilo"]=="Bowl"]

  notas_cup = datos_cup["Nota"]
  notas_pack = datos_pack["Nota"]
  notas_bowl = datos_bowl["Nota"]

  promedio_cup = round(notas_cup.mean(),2)
  promedio_pack = round(notas_pack.mean(),2)
  promedio_bowl = round(notas_bowl.mean(),2)


  return {
    "promedio_cup": promedio_cup,
    "promedio_pack":promedio_pack,
    "promedio_bowl":promedio_bowl
    }

print(analisis_ramen("https://raw.githubusercontent.com/cardel/repositorios/main/mintic/p10/ramen-ratings_publico.csv"))