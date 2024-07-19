#Importar librería json para poder trabajar con esos archivos. 

import json
import os #esta librería evita problemas si el archivo no existe.

def carga_datos(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'r') as file:
            return json.load(file)
    else:
        return {'data': []}

def guarda_datos(archivo, datos):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)

def crea_alumno(datos, cedula, nombre, apellido, nota1, nota2, nota3):
    nuevo_alumno = {
        "cedula": cedula,
        "nombre": nombre,
        "apellido": apellido,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3
    }
    datos['data'].append(nuevo_alumno)

def obten_alumnos(datos):
    return datos['data']

def main():
   #FUNCION PRINCIPAL
    archivo = 'alumnos.json'
    datos = carga_datos(archivo)

    #MENU
    while True:
        print("\nOpciones:")
        print("1. Crear nuevo alumno")
        print("2. Obtener lista de todos los alumnos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cedula = input("Ingrese la cédula: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            nota1 = int(input("Ingrese la nota 1: "))
            nota2 = int(input("Ingrese la nota 2: "))
            nota3 = int(input("Ingrese la nota 3: "))

            crea_alumno(datos, cedula, nombre, apellido, nota1, nota2, nota3)
            guarda_datos("alumnos.json", datos)
            print("Alumno creado correctamente.")

        elif opcion == '2':
            alumnos = obtener_alumnos(datos)
            for alumno in alumnos:
                print(alumno)

        elif opcion == '3':
            break

        else:
            print("Opción no válida. Intente de nuevo.")

