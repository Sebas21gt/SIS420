datos = ["Sebastian Gonzales", "20 años", "Ing. Sistemas", "Barrio Max Toledo"]
hobbies = ["Robotica", "Programacion", "Baile", "Deportes"]

def biografia():
    print("Mi nombre es", datos[0], "tengo", datos[1], "estudio", datos[2])
    print("Voy en 7mo Semestre de mi carrera, Vivo por el",datos[3],"\nMis Hobbies son: \n", hobbies[0] + "\n", hobbies[1] + "\n", hobbies[2] + "\n", hobbies[3] + "\n")

def menu():
    print ("1. Imprimir Biografia")
    print ("2. Salir")
    opcion = int(input("Seleccione la opcion que desea: "))

    if opcion == 1:
        biografia()
    elif opcion == 2:
        print("Programa Finalizado")

biografia()
print ("\n")   
menu()