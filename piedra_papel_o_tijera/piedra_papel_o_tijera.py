# piedra pale o tijera  

import random
print("--------------------")
print("--piedra,papel o tijera-----")

#input
piedra=input
papel=input
tijera=input
# que opccion que deseas realizar
print("piedra")
print("papel")
print("tijera")
yo=input("elige tu opcion:")


opciones=("piedra","papel","tijera")
pc=random.randint(0,2)
pc=opciones[pc]
print("eleccion de la computadora:",pc)
#processing
if (yo==pc):
    print("empate")
if (yo==piedra):
    if(pc==tijera):
        print("ganaste")
    if(pc==papel):
        print("perdiste") 
if (yo==papel):
    if(pc==tijera):
        print("perdiste")
    if(pc==piedra):
        print("ganaste")   
if (yo==tijera):
    if(pc==papel):
        print("ganaste")
    if(pc==piedra):
        print("perdiste")             
        
#fin 
