def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def unidades_categoria(productos, stock, categoria):
    total = 0
    categoria_buscar = categoria.strip().lower()
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria_buscar:
            if codigo in stock:
                total += stock[codigo][1]
    print(f"El total de unidades disponibles es: {total}")

def busqueda_precio(stock, productos, p_min, p_max):
    resultados = []
    for codigo, datos in stock.items():
        precio = datos[0]
        unidades = datos[1]
        if p_min <= precio <= p_max and unidades > 0:
            if codigo in productos:
                nombre = productos[codigo][0]
                resultados.append(f"{nombre}--{codigo}")
    
    if resultados:
        resultados.sort()
        print(f"Los productos encontrados son: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")

def buscar_codigo(productos, codigo):
    return codigo.upper() in productos

def actualizar_precio(productos, stock, codigo, nuevo_precio):
    codigo_up = codigo.upper()
    if buscar_codigo(productos, codigo_up):
        stock[codigo_up][0] = nuevo_precio
        return True
    return False

def validar_no_vacio(texto):
    return bool(texto and texto.strip())

def validar_codigo(productos, codigo):
    if not validar_no_vacio(codigo):
        return False
    return not buscar_codigo(productos, codigo)

def validar_peso(peso_str):
    try:
        peso = float(peso_str)
        return peso > 0
    except ValueError:
        return False

def validar_sn(respuesta):
    return respuesta.strip().lower() in ['s', 'n']

def validar_precio_num(precio_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_unidades(unidades_str):
    try:
        unidades = int(unidades_str)
        return unidades >= 0
    except ValueError:
        return False

def agregar_producto(productos, stock, codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    codigo_up = codigo.upper()
    if buscar_codigo(productos, codigo_up):
        return False
    
    bool_importado = es_importado.lower() == 's'
    bool_cachorro = es_para_cachorro.lower() == 's'
    
    productos[codigo_up] = [nombre, categoria, marca, float(peso_kg), bool_importado, bool_cachorro]
    stock[codigo_up] = [int(precio), int(unidades)]
    return True

def eliminar_producto(productos, stock, codigo):
    codigo_up = codigo.upper()
    if buscar_codigo(productos, codigo_up):
        del productos[codigo_up]
        del stock[codigo_up]
        return True
    return False

def main():
    productos = {
        'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
        'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8.0, False, False],
        'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
        'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
        'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
        'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False]
    }
    
    stock = {
        'M001': [32990, 12],
        'M002': [9990, 0],
        'M003': [5490, 25],
        'M004': [7990, 5],
        'M005': [11990, 7],
        'M006': [24990, 3]
    }
    
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        
        
        opcion = leer_opcion()
        
        if opcion == 1:
            cat = input("Ingrese categoría a consultar: ")
            unidades_categoria(productos, stock, cat)
            
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(stock, productos, p_min, p_max)
                        break
                    else:
                        print("Debe ingresar valores enteros válidos (mínimo menor o igual al máximo)")
                except ValueError:
                    print("Debe ingresar valores enteros")
                    
        elif opcion == 3:
            while True:
                cod = input("Ingrese código del producto: ")
                while True:
                    try:
                        n_precio = int(input("Ingrese nuevo precio: "))
                        if n_precio > 0:
                            break
                        else:
                            print("El precio debe ser un entero positivo")
                    except ValueError:
                        print("Debe ingresar un valor entero")
                
                if actualizar_precio(productos, stock, cod, n_precio):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                
                resp = input("¿Desea actualizar otro precio (s/n)?: ")
                if resp.strip().lower() != 's':
                    break
                    
        elif opcion == 4:
            c_cod = input("Ingrese código del producto: ")
            c_nom = input("Ingrese nombre: ")
            c_cat = input("Ingrese categoría: ")
            c_mar = input("Ingrese marca: ")
            c_pes = input("Ingrese peso (kg): ")
            c_imp = input("¿Es importado? (s/n): ")
            c_cac = input("¿Es para cachorro? (s/n): ")
            c_pre = input("Ingrese precio: ")
            c_uni = input("Ingrese unidades: ")
            
            valido = True
            
            if not validar_codigo(productos, c_cod):
                valido = False
            if not validar_no_vacio(c_nom):
                valido = False
            if not validar_no_vacio(c_cat):
                valido = False
            if not validar_no_vacio(c_mar):
                valido = False
            if not validar_peso(c_pes):
                valido = False
            if not validar_sn(c_imp):
                valido = False
            if not validar_sn(c_cac):
                valido = False
            if not validar_precio_num(c_pre):
                valido = False
            if not validar_unidades(c_uni):
                valido = False
                
            if valido:
                if agregar_producto(productos, stock, c_cod, c_nom, c_cat, c_mar, c_pes, c_imp, c_cac, c_pre, c_uni):
                    print("Producto agregado")
                else:
                    print("El código ya existe")
            else:
                print("Error: Uno o más datos ingresados son inválidos. No se pudo registrar el producto.")
                
        elif opcion == 5:
            cod_eliminar = input("Ingrese código del producto a eliminar: ")
            if eliminar_producto(productos, stock, cod_eliminar):
                print("Producto eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            break

main()