# Investigamos como hacer para convertir los gramos en joules, pero encontramos que son dos tipos de
#unidades diferentes y no hay ninguna conversion concreta, por eso damos por hecho que podemos mezclarlos.
#el calculo que hicimos fue: energiaTom = energiaTom + pesoRaton + joules.

'''
INTEGRANTES DEL GRUPO AVENGERS:
Romina Luna - romiluna04@gmail.com
Gabriela Martinez Soliz - gms.martinez18@gmail.com
Natalia Villafañe - nataliavillafane05@gmail.com
Azucena Panez Campos - azucenadelrosario95@gmail.com'''


import tomFuncion
print("")
print("    ###################################")
print("    #                                 #")
print("    #   Hola!! Bienvenidos a Jugando  #")
print("    #            With Tom!!           #")
print("    #                                 #")
print("    ###################################")
energia= 100
segundos=0
cantRaton=0
distancia=0
raton=1
op=0
validar=0
def start_game():
    start = None
    while start != "S":
        start = input("¿Queres empezar a jugar?: [S/N] ")
        start = start.upper()
        if start == "N":
            print("Media pila loco! nos hiciste codear al pedo!!!")
            exit()
        if start == "S":
            print("Bien!! Veremos lo que pasa con nuestro amigo Tom!!")
start_game()

while(op!=2):
    op=int(input('Querés darle de comer a Tom? 1.Si / 2.No '))
    if(op==1):
        print("Bien!! Veremos lo que pasa con nuestro amigo Tom!!")  
        print('La energia actual de Tom es: ',energia, ' joules')
        pesoRaton = int(input("\nIngrese cuantos gramos pesa el ratón que se comerá Tom: "))
        nombreRaton = str(input("¿Como se llama el ratón?: "))
        print(nombreRaton, "ha sido entregado como tributo a Tom (╥﹏╥) ")
        distancia=int(input('Ingrese la distancia en metro donde esta el ratón '))   
        print('Tom esta evaluando si comer al ratón...')
        validar=tomFuncion.meConvieneComerA(distancia,energia,pesoRaton)
        if(validar==1):
            print('Tom agarra a',nombreRaton,' en ' , tomFuncion.correr(energia,distancia), ' segundos')
            energia=energia-(0.5*distancia)
            print('Tom capturó al ratón!!!!!!!!')
            energia=tomFuncion.comer(energia,pesoRaton)
            print('Tom ganó energía al comerse a ',nombreRaton, '  \nEnergía final:\n',energia, ' joules')
            print('ahora la energia de Tom es: ',energia, ' joules')
        else:
            print(nombreRaton, ' esta muy lejos, Tom prefiere descansar')
    else:
         print("\nAdios!! Tom te extrañará y necesita comer, así que no te tardes mucho en volver!!")