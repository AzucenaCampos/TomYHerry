
def comer (energia,pesoRaton):
    energia1=energia+12+(pesoRaton)
    return energia1
    

def correr (energia,distancia):
    velocidad=5+(energia/10)
    segundos=distancia/velocidad
    return segundos

def meConvieneComerA(distancia,energia,pesoRaton):
    ganancia=pesoRaton+12
    perdida=(0.5*distancia)
    validar=0
    if(ganancia>perdida):
        validar =1
    else:
        validar=0
    return validar
