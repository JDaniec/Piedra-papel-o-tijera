# Piedra papel o tijera
import random
print("-------------------------------------------------------------------")
print("--------------------PIEDRA PAPEL O TIJERA--------------------------")
print("-------------------------------------------------------------------")


#input
print("1 >>> Piedra")
print("2 >>> papel")
print("3 >>> tijera")

Piedra = 1
papel = 2
tijera = 3

d = int(input("Digite la opcion "))
m = random.randint(1, 3)

if 1 <= d <= 3:
    if d == m:
        print("Empate")

    elif d == 1 and m == 3:
        print("Ganaste")

    elif d == 1 and m == 2:
        print("Perdio jaja")

    elif d == 3 and m == 1:
        print("Perdio") 

    elif d == 2 and m == 3:
        print("Perdio")

    elif d == 2 and m == 1:
        print("Ganasteeeee")

    elif d == 3 and m == 2:
        print("Ganaste")
else:
    print("El numero asiganado no corresponde a ninguna opción")


print("La opcion de la maquina fue" + str(m))


