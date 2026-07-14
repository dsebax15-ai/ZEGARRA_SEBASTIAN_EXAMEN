import os
os.system("cls")

productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False]
}

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3]
}




def unidades_categoria(categoria):
    total = 0
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria.lower():
            total += stock[codigo][1]
    print("El total de unidades disponibles es:", total)

def buscar_precio(minimo, maximo):
    lista = []

    for codigo, datos_stock in stock.items():
        precio = datos_stock[0]
        unidades = datos_stock[1]

        if minimo <= precio <= maximo and unidades > 0:
            nombre = productos[codigo][0]
            lista.append(f"{nombre}--{codigo}")

    if len(lista) == 0:
        print("No hay productos en ese rango de precio")
    else:
        lista.sort()
        print("Los productos encontrados son:", lista)

def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper()

    if codigo in stock:
        stock[codigo][0] = nuevo_precio
        return True
    return False

def validar_codigo(codigo):
    return codigo.strip() != ""


def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_categoria(categoria):
    return categoria.strip() != ""


def validar_marca(marca):
    return marca.strip() != ""


def validar_peso(peso):
    return peso > 0


def validar_importado(valor):
    return valor.lower() in ("s", "n")


def validar_perrito(valor):
    return valor.lower() in ("s", "n")


def validar_precio(precio):
    return precio > 0


def validar_unidades(unidades):
    return unidades >= 0

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_perrito, precio, unidades):

    codigo = codigo.upper()

    if codigo in productos:
        return False

    productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_perrito]

    stock[codigo] = [precio, unidades]

    return True

def eliminar_producto(codigo):
    codigo = codigo.upper()

    if codigo in productos:
        del productos[codigo]
        del stock[codigo]
        return True

    return False

while True:

    print("========== Menu principal ==========")
    print("1. Unidades por categoria")
    print("2. Buscar productos por rango de precio")
    print("3. Actualizar precio de productos")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

    op = input("Ingrese opcion: ")

    if op == "1":

        categoria = input("Ingrese categoria a consultar: ")
        unidades_categoria(categoria)

    elif op == "2":

        while True:
            try:
                minimo = int(input("Ingrese precio minimo: "))
                maximo = int(input("Ingrese precio maximo: "))
                break
            except:
                print("Debe ingresar valores enteros")

        if minimo <= maximo and minimo >= 0:
            buscar_precio(minimo, maximo)
        else:
            print("Rango de precios invalido")

    elif op == "3":

        while True:

            codigo = input("Ingrese codigo del producto: ").upper()

            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        break
                    else:
                        print("El precio debe ser mayor que cero")
                except:
                    print("Debe ingresar un numero entero")

            if actualizar_precio(codigo, nuevo_precio):
                print("Precio actualizado")
            else:
                print("El codigo no existe")

            seguir = input("Desea actualizar otro precio (s/n)?: ").lower()

            if seguir == "n":
                break

    elif op == "4":

        codigo = input("Ingrese codigo del producto: ").upper()
        nombre = input("Ingrese nombre: ")
        categoria = input("Ingrese categoria: ")
        marca = input("Ingrese marca: ")

        try:
            peso = float(input("Ingrese peso en kilos(kg): "))
        except:
            peso = -1

        importado = input("Es importado? (s/n): ").lower()
        perrito = input("Es para un perrito? (s/n): ").lower()

        try:
            precio = int(input("Ingrese precio: "))
        except:
            precio = -1

        try:
            unidades = int(input("Ingrese unidades: "))
        except:
            unidades = -1

        if not validar_codigo(codigo):
            print("Codigo invalido")

        elif codigo in productos:
            print("El codigo ya existe")

        elif not validar_nombre(nombre):
            print("Nombre invalido")

        elif not validar_categoria(categoria):
            print("Categoria invalida")

        elif not validar_marca(marca):
            print("Marca invalida")

        elif not validar_peso(peso):
            print("Peso invalido")

        elif not validar_importado(importado):
            print("Valor de importado invalido")

        elif not validar_perrito(perrito):
            print("Valor de cachorro invalido")

        elif not validar_precio(precio):
            print("Precio invalido")

        elif not validar_unidades(unidades):
            print("Unidades invalidas")

        else:

            es_importado = importado == "s"
            es_perrito = perrito == "s"

            if agregar_producto(codigo, nombre, categoria, marca, peso, es_importado, es_perrito, precio, unidades):

                print("Producto agregado")
            else:
                print("El codigo ya existe")

    elif op == "5":

        codigo = input("Ingrese codigo del producto: ")

        if eliminar_producto(codigo):
            print("Producto eliminado")
        else:
            print("El codigo no existe")

    elif op == "6":

        print("Programa finalizado, adios")
        break

    else:
        print("Debe seleccionar una opcion valida")