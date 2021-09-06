import math as Mate
def estudio_credito(valor_solicitado:float, periodo:int)->dict:
    if periodo <= 12:
        interes_total = (3.5 * periodo)/100
        valor_total = valor_solicitado + (valor_solicitado * interes_total)
        valor_cuota = valor_total / periodo
    elif periodo <= 24:
        interes_total= (3 * periodo)/100
        valor_total = valor_solicitado + (valor_solicitado * interes_total)
        valor_cuota = valor_total / periodo
    elif periodo <= 36:
        interes_total= (2.3 * periodo)/100
        valor_total = valor_solicitado + (valor_solicitado * interes_total)
        valor_cuota = valor_total / periodo
    elif periodo > 60:
        interes_total= (1.0 * periodo)/100
        valor_total = valor_solicitado + (valor_solicitado * interes_total)
        valor_cuota = valor_total / periodo
    else:
        interes_total = (1.8 * periodo)/100
        valor_total = valor_solicitado + (valor_solicitado * interes_total)
        valor_cuota = valor_total / periodo
    salida = {
        "valor_cuota":Mate.ceil(valor_cuota),
        "valor_total":valor_total
        }
    return salida