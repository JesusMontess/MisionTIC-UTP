'''
Autor: Jesus Montes
Fecha: 15/Junio/2021
'''
from functools import reduce
 
def calculoBoletas(venta:tuple)->float:
    salas = venta[0]
    tipos = venta[1]
    clientes = venta[2]
    numero_boletas = venta[3]
 
    if salas=="2d" and clientes=="adulto" and tipos=="general":
        return 9500*numero_boletas
    elif salas == "2d" and clientes=="adulto" and tipos =="preferencial":
        return 12000*numero_boletas
    elif salas == "3d" and clientes=="adulto" and tipos =="general":
        return 13000*numero_boletas
    elif salas =="3d" and clientes=="adulto" and tipos =="preferencial":
        return 15000*numero_boletas
    elif salas =="2d" and clientes =="niño" and tipos =="general":
        return 4750*numero_boletas
    elif salas == "2d" and clientes =="niño" and tipos =="preferencial":
        return 6000*numero_boletas
    elif salas == "3d" and clientes =="niño" and tipos =="general":
        return 6500*numero_boletas
    elif salas =="3d" and clientes =="niño" and tipos =="preferencial":
        return 7500*numero_boletas    
    else:
        return 0

def consolidado_cine(ventas:list)->dict:

    venta2D = list(filter(lambda x: x[0]=="2d",ventas))
    venta3D = list(filter(lambda x: x[0]=="3d",ventas))
 
    numero_Boletas_2D = reduce(lambda acc,elm: acc+elm[3],venta2D,0)
    numero_Boletas_3D = reduce(lambda acc,elm: acc+elm[3],venta3D,0) 
 
    if numero_Boletas_3D >= numero_Boletas_2D:
        funciones = "3d"
    else:
        funciones ="2d"

    diferencia_boletas_funcion = abs(numero_Boletas_2D - numero_Boletas_3D)

    ventas_2D = reduce(lambda acc,elm: acc+calculoBoletas(elm),venta2D,0)
    ventas_3D = reduce(lambda acc,elm: acc+calculoBoletas(elm),venta3D,0)

    diferencia_dinero_funcion = abs(ventas_2D - ventas_3D)

    ventas_B_General = list(filter(lambda x: x[1]=="general",ventas))
    ventas_B_Preferencial = list(filter(lambda x: x[1]=="preferencial",ventas))
    
    numero_Boletas_General = reduce(lambda acc,elm: acc+elm[3],ventas_B_General,0)
    numero_Boletas_Preferencial = reduce(lambda acc,elm: acc+elm[3],ventas_B_Preferencial,0) 

    if numero_Boletas_Preferencial >= numero_Boletas_General:
        sala ="preferencial"
    else:
        sala ="general"
    
    diferencia_boletas_sala = abs(numero_Boletas_General - numero_Boletas_Preferencial)

    ventas_General= reduce(lambda acc,elm: acc+calculoBoletas(elm),ventas_B_General,0)
    ventas_Preferencial = reduce(lambda acc,elm: acc+calculoBoletas(elm),ventas_B_Preferencial,0)
 
    diferencia_dinero_sala =abs(ventas_General - ventas_Preferencial)

    ventasNiño = list(filter(lambda x: x[2]=="niño",ventas))
    ventasAdultos = list(filter(lambda x: x[2]=="adulto",ventas))
    
    numeroBoletas_Adultos = reduce(lambda acc,elm: acc+elm[3],ventasAdultos,0)
    numeroBoletas_Niños = reduce(lambda acc,elm: acc+elm[3],ventasNiño,0)
     
    
    if numeroBoletas_Adultos >= numeroBoletas_Niños:
         cliente = "adulto"
    else:
        cliente = "niño"
    
    ventas_B_Adulto= reduce(lambda acc,elm: acc+calculoBoletas(elm),ventasAdultos,0)
    ventas_B_Niños = reduce(lambda acc,elm: acc+calculoBoletas(elm),ventasNiño,0)
 
    diferencia_boletas_cliente = abs(numeroBoletas_Adultos - numeroBoletas_Niños)
    diferencia_dinero_cliente  = abs(ventas_B_Adulto-ventas_B_Niños)

    salida = {
        "funcion": funciones,
 "diferencia-boletas-funcion": diferencia_boletas_funcion,
 "diferencia-dinero-funcion": diferencia_dinero_funcion,
 "sala": sala,
 "diferencia-boletas-sala": diferencia_boletas_sala,
 "diferencia-dinero-sala": diferencia_dinero_sala,
 "cliente": cliente,
 "diferencia-boletas-cliente": diferencia_boletas_cliente,
 "diferencia-dinero-cliente": diferencia_dinero_cliente,

    }

    return salida

print(consolidado_cine([ ("2d","general","adulto",10),
 ("2d","general","niño",4) ,
 ("3d","preferencial","niño",8) ,
 ("3d","preferencial","adulto",6) ,
 ("2d","preferencial","adulto",7) ,
 ("2d","general","adulto",10) ,
 ("2d","preferencial","adulto",13) ,
 ("3d","general","niño",12) ,
 ("3d","preferencial","niño",12) ]))
