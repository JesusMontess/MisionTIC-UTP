"""
Autor: Jesus Montes
Fecha: 06/junio/2021
----------------------------------------------------------
 produccion_te_gas: tupla de 12 números que indican la
producción de té con gas
 produccion_te_sin_gas: tupla de 12 números que indican la
producción de té sin gas
 retorno: diccionario.
 {"total_te_gas":total_te_gas,
 "costo_prod_te_gas":costo_prod_te_gas,
 "ing_te_gas":ing_te_gas,
 "ganancia_te_gas":ganancia_te_gas,
 "total_te_sin_gas":total_te_sin_gas,
 "costo_prod_te_sin_gas":costo_prod_te_sin_gas,
 "ing_te_sin_gas":ing_te_sin_gas,
 "ganancia_te_sin_gas":ganancia_te_sin_gas,
 "costo_prod_total": costo_prod_total,
 "ing_total": ing_total,
 "ganancia_total", ganancia_total}
 """
def resumen_producion(produccion_te_gas: tuple,
produccion_te_sin_gas: tuple) -> dict:
    costo_producir_te_con_gas = 600
    costo_producir_te_sin_gas = 320
    precio_venta_te_con_gas = 3100
    precio_venta_te_sin_gas = 2200
    ganancias_te_gas = precio_venta_te_con_gas - costo_producir_te_con_gas
    ganancias_te_sin_gas = precio_venta_te_sin_gas -costo_producir_te_sin_gas
    total_te_gas = sum((produccion_te_gas))
    total_te_sin_gas = sum((produccion_te_sin_gas))
    costo_prod_te_gas = costo_producir_te_con_gas * total_te_gas
    ing_te_gas = precio_venta_te_con_gas * total_te_gas
    ganancia_te_gas = ganancias_te_gas * total_te_gas
    costo_prod_te_sin_gas = costo_producir_te_sin_gas * total_te_sin_gas
    ing_te_sin_gas = precio_venta_te_sin_gas * total_te_sin_gas
    ganancia_te_sin_gas = ganancias_te_sin_gas * total_te_sin_gas
    costo_prod_total = costo_prod_te_gas + costo_prod_te_sin_gas
    ing_total = ing_te_gas + ing_te_sin_gas
    ganancia_total = ganancia_te_gas + ganancia_te_sin_gas

    mensaje = {
    "total_te_gas":total_te_gas,
    "costo_prod_te_gas":costo_prod_te_gas,
    "ing_te_gas":ing_te_gas,
    "ganancia_te_gas":ganancia_te_gas,
    "total_te_sin_gas":total_te_sin_gas,
    "costo_prod_te_sin_gas":costo_prod_te_sin_gas,
    "ing_te_sin_gas":ing_te_sin_gas,
    "ganancia_te_sin_gas":ganancia_te_sin_gas,
    "costo_prod_total": costo_prod_total,
    "ing_total": ing_total,
    "ganancia_total": ganancia_total 
    }
    return mensaje

print(resumen_producion((200, 200, 300, 800, 200, 300, 100, 4,
841, 120, 121, 45),(172, 200, 450, 120, 121, 184, 233, 155, 852,
400, 101, 17)))









