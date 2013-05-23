print("Busqueda Binaria")

n = int(input("Ingrese cantidad total de la lista: "))    # Se pide el total de elementos y se ingresan como entero a 'n'.
naux = n    # Se guarda el total en una variable auxiliar para ingresar los datos sin perder el valor.
lista = []    # Se crea una lista vacía para ingresar los datos.

print("Nota: Los datos a ingresar deben estar ordenados de menor a mayor.")
while naux > 0:    # Mientras el total de elementos sea mayor a cero se pediran datos a ingresar.
    lista.append(input("Ingrese dato: "))    # Se van ingresando los datos a la lista uno por uno.
    naux -= 1    # Al total de los valores se les descuenta uno en cada ciclo.

dato = input("Ingrese dato a buscar: ")    # Se pide el valor a buscar.

# Función de busqueda binaria.
def busca_d(lista, dato, ini, fin):
    while ini <= fin:    # Mientras el inicio sea menor o igual a fin el ciclo se recorera.
        mitad = int((ini + fin)/2)    # Se calcula el valor central de la lista.
        if lista[mitad] == dato:    # Si el valor de la mitad es igual al dato pedido se retorna True.
            return True
        elif lista[mitad] > dato:    # Si el dato es menor que el valor de la mitad...
            fin = mitad - 1    # ...'fin' cambia su valor a mitad menos 1 para revisar solo el lado izquierdo de la lista.
        else:    # Si el dato es mayor que el valor central...
            ini = mitad + 1    # ...'ini' cambia su valor a mitad mas uno para buscar entre los valores mayores de la derecha.
    return False    # Si el valor no es encontrado en la lista se retorna un False.

if busca_d(lista, dato, 0, n - 1):    # Se llama a la función de busqueda binaria con inicio en cero y fin en el total de elementos de la lista.
    # Si la función retorna True se encontro el dato en la lista.
    print("El dato", dato, "se encontró en la lista.")
else:    # Sino el dato no estaba en la lista ingresada.
    print("El dato", dato, "NO se encuentra en la lista.")
