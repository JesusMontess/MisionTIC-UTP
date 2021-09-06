'''
Autor: Jesus Montes
Fecha: 15/Junio/2021
'''
from functools import reduce
 
def calcular_boleta(venta:tuple)->float:
    sala = venta[0]
    tipo = venta[1]
    cliente = venta[2]
    num_boletas = venta[3]
 
    if sala=="2d" and cliente=="adulto" and tipo=="general":
        return 9500*num_boletas
    elif sala == "2d" and cliente=="adulto" and tipo=="preferencial":
        return 12000*num_boletas
    elif sala == "3d" and cliente=="adulto" and tipo=="general":
        return 13000*num_boletas
    elif sala =="3d" and cliente=="adulto" and tipo=="preferencial":
        return 15000*num_boletas
    elif sala=="2d" and cliente=="niño" and tipo=="general":
        return 4750*num_boletas
    elif sala == "2d" and cliente=="niño" and tipo=="preferencial":
        return 6000*num_boletas
    elif sala == "3d" and cliente=="niño" and tipo=="general":
        return 6500*num_boletas
    elif sala =="3d" and cliente=="niño" and tipo=="preferencial":
        return 7500*num_boletas    
    else:
        return 0
 
 
def consolidado_cine(ventas:list)->dict:
    salida = {}
 
    venta2D = list(filter(lambda x: x[0]=="2d",ventas))
    venta3D = list(filter(lambda x: x[0]=="3d",ventas))
 
    numBoletas_2D = reduce(lambda acc,elm: acc+elm[3],venta2D,0)
    numBoletas_3D = reduce(lambda acc,elm: acc+elm[3],venta3D,0) 
 
    if numBoletas_3D >= numBoletas_2D:
        salida["funcion"]="3d"
    else:
        salida["funcion"]="2d"
 
    salida["diferencia-boletas-funcion"]=abs(numBoletas_2D-numBoletas_3D)
 
    ventas_2D = reduce(lambda acc,elm: acc+calcular_boleta(elm),venta2D,0)
    ventas_3D = reduce(lambda acc,elm: acc+calcular_boleta(elm),venta3D,0)
 
    salida["diferencia-dinero-funcion"]=abs(ventas_2D-ventas_3D)
    
    #Tipo de zona
    ventaGeneral = list(filter(lambda x: x[1]=="general",ventas))
    ventaPreferencial = list(filter(lambda x: x[1]=="preferencial",ventas))
    
    numBoletas_General = reduce(lambda acc,elm: acc+elm[3],ventaGeneral,0)
    numBoletas_Preferencial = reduce(lambda acc,elm: acc+elm[3],ventaPreferencial,0) 
    if numBoletas_Preferencial >= numBoletas_General:
        salida["sala"]="preferencial"
    else:
        salida["sala"]="general"
    
    salida["diferencia-boletas-sala"]=abs(numBoletas_General-numBoletas_Preferencial)
 
    ventas_General= reduce(lambda acc,elm: acc+calcular_boleta(elm),ventaGeneral,0)
    ventas_Preferencial = reduce(lambda acc,elm: acc+calcular_boleta(elm),ventaPreferencial,0)
 
    salida["diferencia-dinero-sala"]=abs(ventas_General-ventas_Preferencial)
    
    #Tipo de cliente
    ventaNihno = list(filter(lambda x: x[2]=="niño",ventas))
    ventaAdulto = list(filter(lambda x: x[2]=="adulto",ventas))
    
    numBoletas_Nihno = reduce(lambda acc,elm: acc+elm[3],ventaNihno,0)
    numBoletas_Adulto = reduce(lambda acc,elm: acc+elm[3],ventaAdulto,0) 
    
    if numBoletas_Adulto >= numBoletas_Nihno:   
         salida["cliente"]="adulto"
    else:
        salida["cliente"]="niño"
 
    ventas_B_Adulto= reduce(lambda acc,elm: acc+calcular_boleta(elm),ventaAdulto,0)
    ventas_B_Niños = reduce(lambda acc,elm: acc+calcular_boleta(elm),ventaNihno,0)
 
    salida["diferencia-boletas-cliente"]=abs(numBoletas_Adulto-numBoletas_Nihno)
    salida["diferencia-dinero-cliente"]=abs(ventas_B_Adulto-ventas_B_Niños)
    return salida
