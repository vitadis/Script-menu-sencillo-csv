#Este ejercicio tiene que ser capaz de agregar y crear nuevos usuarios en csv
#   - Solucionar las excepciones
import pandas as pd

def crear_csv(ruta,df):
    df.to_csv(ruta,index=False)

def datos(archivo,nombre,apellido,edad):
    df = pd.read_csv(archivo)
    datos = pd.DataFrame({"Nombre":nombre,"Apellido":apellido,"Edad":edad},index=[3])
    df = pd.concat([df,datos]).reset_index(drop=True)
    crear_csv(archivo,df)

def añadir(): 
    salir = ""
    var = input("Dime la ruta de tu archivo: ")
    while salir != "n":
        var1 = input("Nombre: ")
        var2 = input("Apellido: ")
        var3 = int(input("Edad: "))
        datos(var,var1,var2,var3)
        salir = input("Deseas continuar s/n: ")
    menu()


def leer():
    var = input("Dime el archivo: ")
    print(pd.read_csv(var))
    menu()

def menu():
    print("Menu CSV\n1.Leer\n2.Agregar\n3:Salir")
    var = input("Selecciona una opción: ")
    match var:
        case "1":
            leer()
        case "2":
            añadir()
        case "3":
            pass
        case _:
            menu()

menu()
