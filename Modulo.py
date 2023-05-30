import random
import os
import csv
import datetime

datos_usuario = {}

def generar_codigo():
    codigo = random.randint(100, 999)
    return codigo

def main_menu():
    while True:
        os.system("cls")
        print("===========================================")
        print("     ***  SYSTEM E-CARD AGUACHICA  ***    ")
        print("                                           ")
        print("1.   -   Comprar tarjeta")
        print("2.   -   Recargar tarjeta")
        print("3.   -   Consultar tarjetas activas")
        print("4.   -   Consultar tarjetas inactivas")
        print("5.   -   Consultar recargas por fecha")
        print("6.   -   Buscar usuario")
        print("7.   -   Buscar una tarjeta")
        print("8.   -   Salir del programa")
        print("============================================")
        try:
            opcion = int(input("Ingrese la opción que desea utilizar: "))
        except ValueError:
            print("Ingresa una opción válida.")
            continue
        
        if opcion == 1:
            comprar_tarjeta()
        elif opcion == 2:
            recargar_tarjeta()
        elif opcion == 3:
            consultar_tarjetas_activas()
        elif opcion == 4:
            consultar_tarjetas_inactivas()
        elif opcion == 5:
            consultar_recargas_por_fecha()
        elif opcion == 6:
            buscar_usuario()
        elif opcion == 7:
            buscar_tarjeta()
        elif opcion == 8:
            print("SALIENDO...")
            exit()

def buscar_tarjeta_usuario():
    os.system("cls")
    print("*** BÚSQUEDA DE TARJETA DE USUARIO ***\n")
    try:
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        if nombre_usuario in datos_usuario:
            tarjetas = datos_usuario[nombre_usuario]
            tarjeta = tarjetas[0]
            print("Tarjeta encontrada:")
            print(f"Usuario: {nombre_usuario}")
            print(f"Código de tarjeta: {tarjeta['numero']}")
            print(f"Saldo: {tarjeta['saldo']}")
            return tarjetas
        else:
            print("No se encontró la tarjeta de usuario.")
    except KeyError:
        print("Error: Nombre de usuario inválido.")

def crear_archivo():
    with open('datos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['nombre', 'fecha', 'codigo', 'saldo'])
        for usuario, tarjetas in datos_usuario.items():
            for tarjeta in tarjetas:
                nombre = usuario
                fecha = tarjeta['fecha_compra'].strftime("%Y-%m-%d")
                codigo = tarjeta['numero']
                saldo = tarjeta['saldo']
                writer.writerow([nombre, fecha, codigo, saldo])

def comprar_tarjeta():
    os.system("cls")
    print("* COMPRA DE TARJETA *")
    print("                         ")
    nombre = input("Ingrese su nombre completo: ")
    
    if nombre in datos_usuario:
        tarjetas = datos_usuario[nombre]
        cantidad_tarjetas = len(tarjetas)
        
        print(f"Ya tienes {cantidad_tarjetas} tarjeta(s) registrada(s).")
        
        if cantidad_tarjetas > 0:
            comprar_otra = input("¿Deseas comprar otra tarjeta con saldo en 0? (S/N): ")
            if comprar_otra.lower() == 's':
                codigo = generar_codigo()
                tarjeta = {
                    "numero": codigo,
                    "fecha_compra": datetime.date.today(),
                    "saldo": 0
                }
                tarjetas.append(tarjeta)
                print(f"Código de tarjeta: {tarjeta['numero']}")
                print("Tarjeta comprada exitosamente.")
                generar_archivo_csv()
                input("Presione Enter para continuar...")
                main_menu()
                return
    
    codigo = generar_codigo()
    tarjeta = {
        "numero": codigo,
        "fecha_compra": datetime.date.today(),
        "saldo": 0
    }
    datos_usuario.setdefault(nombre, []).append(tarjeta)
    
    print(f"Código de tarjeta: {tarjeta['numero']}")
    print("Tarjeta comprada exitosamente.")
    generar_archivo_csv()
    input("Presione Enter para continuar...")
    main_menu()

def generar_archivo_csv():
    try:
        with open('tarjetas.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Número', 'Nombre', 'Código', 'Fecha'])
            for nombre, tarjetas in datos_usuario.items():
                for i, tarjeta in enumerate(tarjetas, 1):
                    numero = i
                    codigo = tarjeta['numero']
                    fecha = tarjeta['fecha_compra'].strftime("%Y-%m-%d")
                    writer.writerow([numero, nombre, codigo, fecha])
        print("Archivo CSV generado exitosamente.")
    except IOError:
        print("Error al generar el archivo CSV. Asegúrate de tener permisos de escritura.")

def recargar_tarjeta():
    os.system("cls")
    print("*** RECARGA DE TARJETA ***")
    print("                         ")
    tarjetas = buscar_tarjeta_usuario()
    if tarjetas:
        print("Tarjetas registradas:")
        for i, tarjeta in enumerate(tarjetas, 1):
            print(f"{i}. Código de tarjeta: {tarjeta['numero']} - Saldo: {tarjeta['saldo']}")
        try:
            opcion = int(input("Seleccione el número de tarjeta que desea recargar: "))
            if opcion >= 1 and opcion <= len(tarjetas):
                tarjeta_seleccionada = tarjetas[opcion - 1]
                valor = float(input("Ingrese cuánto desea recargar: "))
                saldo_actual = tarjeta_seleccionada.get("saldo", 0)
                nuevo_saldo = saldo_actual + valor
                tarjeta_seleccionada["saldo"] = nuevo_saldo
                print(f"¡Tarjeta recargada con éxito! Valor: {valor}")
                print(f"Nuevo saldo de la tarjeta {tarjeta_seleccionada['numero']}: {nuevo_saldo}")
                crear_archivo()
            else:
                print("Opción inválida.")
        except (ValueError, IndexError):
            print("Opción inválida.")
    else:
        print("No se pueden recargar tarjetas. No se encontraron tarjetas registradas.")
        input("Presione Enter para continuar...")
    main_menu()

def consultar_tarjetas_activas():
    os.system("cls")
    print("*** CONSULTA DE TARJETAS ACTIVAS ***")
    print("                         ")
    if datos_usuario:
        for nombre, tarjetas in datos_usuario.items():
            if tarjetas:
                print(f"Cliente: {nombre}")
                print("Tarjetas:")
                for tarjeta in tarjetas:
                    print(f"Código de tarjeta: {tarjeta['numero']} - Saldo: {tarjeta['saldo']}")
            else:
                print(f"Cliente: {nombre} - No tiene tarjetas registradas.")
    else:
        print("No hay clientes registrados.")
    
    input("Presione Enter para continuar...")
    main_menu()

def consultar_tarjetas_inactivas():
    os.system("cls")
    print("*** CONSULTA DE TARJETAS INACTIVAS ***")
    print("                         ")
    if datos_usuario:
        for nombre, tarjetas in datos_usuario.items():
            if not tarjetas:
                print(f"Cliente: {nombre} - No tiene tarjetas registradas.")
    else:
        print("No hay clientes registrados.")
    
    input("Presione Enter para continuar...")
    main_menu()

def consultar_recargas_por_fecha():
    os.system("cls")
    print("*** CONSULTA DE RECARGAS POR FECHA ***")
    print("                         ")
    try:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        datetime.datetime.strptime(fecha, "%Y-%m-%d")
        recargas = []
        with open('datos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                row_fecha = row[1]
                if row_fecha == fecha:
                    recargas.append(row)
        
        if recargas:
            print("Recargas encontradas:")
            for recarga in recargas:
                nombre = recarga[0]
                codigo = recarga[2]
                saldo = recarga[3]
                print(f"Cliente: {nombre} - Código de tarjeta: {codigo} - Saldo: {saldo}")
        else:
            print("No se encontraron recargas para la fecha especificada.")
    except ValueError:
        print("Fecha inválida.")
    
    input("Presione Enter para continuar...")
    main_menu()

def buscar_usuario():
    try:
        usuarios = set()
        with open('datos.csv', mode='a+') as file:
            if file.tell() == 0:
                writer = csv.writer(file)
                writer.writerow(['nombre', 'fecha', 'codigo', 'saldo'])
            else:
                file.seek(0)
                reader = csv.reader(file)
                next(reader)  # Saltar la primera línea (encabezados)
                for row in reader:
                    usuario = row[0]
                    usuarios.add(usuario)
        if usuarios:
            print("Usuarios registrados:")
            for usuario in usuarios:
                print(usuario)
        else:
            print("No hay usuarios registrados.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos.")

def buscar_tarjeta():
    os.system("cls")
    print("*** BÚSQUEDA DE TARJETA ***\n")
    try:
        codigo_tarjeta = int(input("Ingrese el código de tarjeta: "))
        for tarjetas in datos_usuario.values():
            for tarjeta in tarjetas:
                if tarjeta['numero'] == codigo_tarjeta:
                    nombre_usuario = get_nombre_usuario(tarjetas)
                    print("Tarjeta encontrada:")
                    print(f"Usuario: {nombre_usuario}")
                    print(f"Código de tarjeta: {tarjeta['numero']}")
                    print(f"Saldo: {tarjeta['saldo']}")
                    return
        print("No se encontró la tarjeta.")
    except ValueError:
        print("Código de tarjeta inválido.")
    
    input("Presione Enter para continuar...")
    main_menu()

def get_nombre_usuario(tarjetas):
    for nombre, tarjeta in datos_usuario.items():
        if tarjetas == tarjeta:
            return nombre

def cargar_datos():
    try:
        with open('datos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                nombre = row[0]
                fecha = datetime.datetime.strptime(row[1], "%Y-%m-%d").date()
                codigo = int(row[2])
                saldo = float(row[3])
                tarjeta = {
                    "numero": codigo,
                    "fecha_compra": fecha,
                    "saldo": saldo
                }
                datos_usuario.setdefault(nombre, []).append(tarjeta)
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Se creara uno nuevo al guardar la información.")

def guardar_datos():
    try:
        with open('datos.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['nombre', 'fecha', 'codigo', 'saldo'])
            for usuario, tarjetas in datos_usuario.items():
                for tarjeta in tarjetas:
                    nombre = usuario
                    fecha = tarjeta['fecha_compra'].strftime("%Y-%m-%d")
                    codigo = tarjeta['numero']
                    saldo = tarjeta['saldo']
                    writer.writerow([nombre, fecha, codigo, saldo])
    except IOError:
        print("Error al guardar los datos. Asegúrate de tener permisos de escritura.")

cargar_datos()
main_menu()
guardar_datos()
