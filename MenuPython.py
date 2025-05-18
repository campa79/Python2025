### Menu con Ejemplos en Python ###
### AC 17/5/25 v1.0 Beta        ###

import random

def menu():
    print("[1] - Generar 10 Números Aleatorios del 1 al 100")
    print("[2] - Sorteo Concurso 1 Ganador")
    print("[3] - Armar Equipo de Dobles en Paddle al Azar")
    print("[4] - Opción 4")
    print("[0] - Salir del Programa")

def option4():
    print("Opción 4 llamada correctamente usando una función")

menu()
option = int(input("Ingresar la Opción: "))

while option != 0:
    if option == 1:
        print("Los 10 números son:")
        for i in range(10):
            print(random.randint(1, 100))
    elif option == 2:
        sorteo = ["Beto","Roberto","Pepe","Luciano","Santiago","Laika","Pancrasia"]
        print("El ganador es: ", random.choice(sorteo))
    elif option == 3:
        print("Opción 3 elegida correctamente.")
        sorteoPaddle = ["Beto","Roberto","Pepe","Luciano","Santiago","Laika","Pancrasia","Mariano","Lucas","Ermenegilda"]
        #random.sample(sorteoPaddle, 4)
        print("Las Parejas de Paddle serán: ", random.sample(sorteoPaddle, 4))
    elif option == 4:
        option4()
    else:
        print("Opción inválida.")

    print()
    menu()
    option = int(input("Ingresar la Opción: "))

print("Gracias por usar este menu!")

