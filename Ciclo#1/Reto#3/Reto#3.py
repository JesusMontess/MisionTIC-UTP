def resumen_producion(produccion_te_gas: tuple, produccion_te_sin_gas: tuple) -> dict:
    salida = {}
 
    total_te_gas = 0
    for elm in produccion_te_gas:
        total_te_gas+=elm
    
    costo_prod_te_gas=total_te_gas*600
    int_te_gas= total_te_gas*3100
    ganancias_te_gas = int_te_gas-costo_prod_te_gas
 
    salida["total_te_gas"]=total_te_gas
    salida["costo_prod_te_gas"]=costo_prod_te_gas
    salida["ing_te_gas"]=int_te_gas
    salida["ganancia_te_gas"]=ganancias_te_gas
 
    #Te sin gas
    total_te_sin_gas = 0
    for elm in produccion_te_sin_gas:
        total_te_sin_gas+=elm
    
    costo_prod_te_sin_gas=total_te_sin_gas*320
    int_te_sin_gas= total_te_sin_gas*2200
    ganancias_te_sin_gas = int_te_sin_gas-costo_prod_te_sin_gas
 
    salida["total_te_sin_gas"]=total_te_sin_gas
    salida["costo_prod_te_sin_gas"]=costo_prod_te_sin_gas
    salida["ing_te_sin_gas"]=int_te_sin_gas
    salida["ganancia_te_sin_gas"]=ganancias_te_sin_gas
 
    #Totales
    costo_prod_total = costo_prod_te_gas+costo_prod_te_sin_gas
    salida["costo_prod_total"]=costo_prod_total
 
    ing_total=int_te_gas+int_te_sin_gas
    salida["ing_total"]=ing_total
 
    ganancia_total=ganancias_te_gas+ganancias_te_sin_gas # ing_total - costo_prod_total
 
    salida["ganancia_total"]=ganancia_total
    """
    Tambien puede hacerse asi.
    {{"total_te_gas": total_te_gas,"costo_prod_te_gas": costo_prod_te_gas,"ing_te_gas": ing_te_gas,"ganancia_te_gas": ganancia_te_gas,
    "total_te_sin_gas": total_te_sin_gas,"costo_prod_te_sin_gas": costo_prod_te_sin_gas,"ing_te_sin_gas": ing_te_sin_gas,
    "ganancia_te_sin_gas": ganancia_te_sin_gas,"costo_prod_total": costo_prod_total,"ing_total": ing_total,"ganancia_total": ganancia_total}}
    """
    return salida