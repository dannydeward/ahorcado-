import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_válida(palabras):
    #seleccionar una palabra al azar de la lista de palabras
    palabra=random.choice(palabras)

    while'_' in palabra or ' ' in palabra:
        palabra=random.choice(palabras)

    return palabra.upper()

def ahorcado():


    print("*********************************")
    print("BIENVENIDO AL JUEGO DEL AHORCADO")
    print("*********************************")

    palabra= obtener_palabra_válida(palabras)

    letras_por_adivinar=set(palabra)
    letras_adivinadas= set()
    abecedario=set(string.ascii_uppercase)

    vidas=7

    while len(letras_por_adivinar) >0 and vidas >0:
         print(f"te quedan {vidas} vidas y has usado estas letras:{' '.join(letras_adivinadas)}")
         
         palabra_lista=[letra if letra in letras_adivinadas else '_' for letra in palabra]
         print(vidas_diccionario_visual[vidas])
         print(f"palabra: {' '.join(palabra_lista)}")

         letra_usuario= input("escoge una letra:  ").upper()

         if letra_usuario in abecedario-letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
               letras_por_adivinar.remove(letra_usuario)
               print(" ")
            else:
                 vidas= vidas-1
                 print(f"\nTu letra,{letra_usuario}, no esta en la palabra")


         elif letra_usuario in letras_adivinadas:
             print("ya escogiste esa letra, por favor ingresa una letra nueva")
         else:
             print("la letra ingresada no es valida, ingresa otra")

    if  vidas==0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado perdiste, lo lamento mucho, la palabra era: {palabra}")
    else:
        print(f" Excelente adivinaste la palabra {palabra}")



ahorcado()
      
  
