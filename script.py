import pandas as pd
import excepciones as exc #Este modulo que cremos contiene funciones para tratar posibles excepciones
from pathlib import Path
"""
IMPORTANTE SI O SI EL CSV TIENE QUE TENER UNA COLUMNA LLAMADA "Id"
- Recuerda que la ruta de un archivo en python depende del dispositivo.
"""

#Menu 1 creacion de df e incorporacion a la tabla de manera instantanea
def menu_1(df_archivo,nombre_archivo):
    df = pd.DataFrame([{}])
    for x in df_archivo.columns:
        if df_archivo[x].dtype == 'int64':
            fila = exc.exc_intput(f"{x}: ")
            df[x]=fila
        elif df_archivo[x].dtype == 'bool':
            fila = bool(input(f"{x} (solo True or False): "))
            df[x]=fila
        elif df_archivo[x].dtype == 'float64':
            fila = float(input(f"{x} (Solo float): "))
            df[x]=fila
        else:
            fila = input(f"{x}: ")
            df[x]=fila
    df_archivo = pd.concat([df_archivo,df],axis= 0)
    df_archivo.to_csv(nombre_archivo,index=False)
            
    

#Menu Bucle 
flag = True
while True:
    
    #Creamos un flag para que esta parte de codigo solo pueda repetir una sola vez.
    if flag:
        
        #Pedimos el archivo
        archivo = input("Agrega la ruta y nombre de tu csv: ")
        nom_archivo = archivo
        archivo_path = Path(archivo)
        
        #Validamos que el archivo exista en caso de no existir este nos hara crear uno nuevo
        if archivo_path.is_file():
            archivo = pd.read_csv(archivo)
        else:
            var0 = exc.exc_intput("Dame el numero de columnas: ")
            df = pd.DataFrame({})
            df["Id"] = 0
            for x in range(var0-1):
                colu = input("Dame el nombre de columna: ")
                coludat = input("Agrega el tipo de dato int/str/float/bool : ")
                if coludat == "int": df[colu] = 0
                elif coludat == "str": df[colu] = ""
                elif coludat == "float": df[colu] = 0.00
                elif coludat == "bool": df[colu] = False
                else: df[colu] = "Nan"
            df.to_csv(archivo,index=False)
            archivo = pd.read_csv(archivo)
        flag = False
    
    #Menu impreso 
    print("""
------ Menu ------
1. Agrega df al archivo
2. Eliminar usuario
3. Ver usuario
4. Cambiar datos
5. Filtrar datos
""") #En espera de crear más menus
    var1 = exc.exc_intput("Elige una opción: ") #Manejo de excepciones de tipo int 
    match var1:
        
        #Menu 1
        case 1:
            var3=exc.exc_intput("Dime cuantos usuarios deseas agregar: ") #Segun los digitos que ponga aqui se realizara el bucle
            for x in range(var3):
                archivo = pd.read_csv(nom_archivo)
                menu_1(archivo,nom_archivo)
        case 2:
            var4 = exc.exc_intput("Dime el id del usuario: ")
            #Buscara el id del usuario en caso de que no retornara el mensaje abajo de else y volvera al menu
            if var4 in archivo["Id"].tolist():
                indice = archivo.index[archivo["Id"] == var4][0]
                archivo = archivo.drop(indice).reset_index(drop=True)
                archivo.to_csv(nom_archivo,index=False)
            else:
                print("No se encontro ningun dato")
        case 3:
            var5 = exc.exc_intput("Dime el id del usuario: ")
            #Realiza la misma busqueda que la de arriba e imprime el usuario si lo encontro
            if var5 in archivo["Id"].tolist():
                print(archivo[archivo["Id"]==var5])
            else: print("No existe ningun usuario con ese id")
        case 4:
            var6 = exc.exc_intput("Dime el id del usuario: ")
            #Si encuentra el id hace lo siguiente
            if var6 in archivo["Id"].tolist():
                var7 = " ".join(archivo.columns.tolist()[1:])
                while True:
                    #La siguiente var nos muestra una lista ya separada en la que se encuentra las columnas de nuestro df
                    pregunta = input(f"Que quieres cambiar {var7}: ")    
                    #Si el usuario no agrega una columna existente el bucle continuara hasta que lo haga
                    if pregunta in archivo.columns:
                        indice = archivo.index[archivo["Id"] == var6][0] #Sacamos el indice del con el id del usuario
                        var8 = input(f"Nuevo {pregunta}: ")
                        archivo.at[indice,pregunta] = var8 #Ahora lo que hacemos es cambiar tomando el indice y la columna que deceamos cambiar
                        archivo.to_csv(nom_archivo,index=False)
                        break #Terminado esto el bucle se cierra
                    else: print("Selecciona una opcion valida")     
            else: print("No existe ningun usuario con ese id")
        case 5:   
            pass
        case _:
            pass
