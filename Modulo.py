data = {}
import csv

def principal():
    while True:
        print("SISTEMA DE REGISTRO DE DATOS")
        print("1. Escribir encabezado")
        print("2. Pedir datos")
        print("3. Escribir datos en el archivo")
        print("4. Leer datos del archivo")
        print("5. Salir del programa")
        opcion = input("Elige una opcion: ")
        try:
            if opcion == "1":
                write_F_names()
            elif opcion == "2":
                data = get_data()
            elif opcion == "3":
                write_file(data)
            elif opcion == "4":
                readfile()
            elif opcion == "5":
                print("SALIENDO..")
                exit()
            else:
                print("ERROR EN LA OPCION")
        except ValueError:
            print("ERROR")

def get_data():
    try:
        cedula = int(input("Cedula: "))
        nombre = input("Nombre: ")
        ciudad = input("Ciudad: ")
        edad = int(input("Edad: "))
        data["cedula"] = cedula
        data["nombre"] = nombre
        data["ciudad"] = ciudad
        data["edad"] = edad
    except ValueError:
        print("ERROR")
    return data

def write_file(data):
    lista = ["cedula", "nombre", "ciudad", "edad"]
    with open("data.txt", "a", encoding="utf-8", newline='') as f:
        write = csv.DictWriter(f, fieldnames=lista)
        write.writerow(data)

def write_F_names():
    lista = ["cedula", "nombre", "ciudad", "edad"]
    with open("data.txt", "a", encoding="utf-8", newline='') as f:
        write = csv.DictWriter(f, fieldnames=lista, quotechar='"')
        write.writeheader()

def readfile():
    with open("data.txt", encoding="utf-8") as f:
        csvdreader = csv.DictReader(f, delimiter=",")
        for row in csvdreader:
            print(f"{row['cedula']} - {row['nombre']} - {row['ciudad']} - {row['edad']}") 
