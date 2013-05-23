print("Busqueda Binaria")

n = int(input("Ingrese cantidad total de la lista: "))    # Se pide el total de elementos y se ingresan como entero a 'n'.
naux = n    # Se guarda el total en una variable auxiliar para ingresar los datos sin perder el valor.
lista = []    # Se crea una lista vacía para ingresar los datos.

print("Nota: Los datos a ingresar deben estar ordenados de menor a mayor.")
while naux > 0:    # Mientras el total de elementos sea mayor a cero se pediran datos a ingresar.
    lista.append(input("Ingrese dato: "))    # Se van ingresando los datos a la lista uno por uno.
    naux -= 1    # Al total de los valores se les descuenta uno en cada ciclo.

dato = input("Ingrese dato a buscar: ")    # Se pide el valor a buscar.

# Función de busqueda binaria recursiva.
def busca_d(lista, dato, ini, fin):
    if ini <= fin:    # Si el punto de inicio de la lista es menor o igual al final indica que ya se recorrio toda la lista.
        mitad = int((ini + fin)/2)    # Sino se ha recorrido la lista completa aun se calcula la mitad de esta.
        if lista[mitad] == dato:    # Si el valor de la posicion del medio es igual al dato ingresado a buscar se retorna que esta.
            return True
        elif lista[mitad] > dato:    # Si el dato es menor que el dato de la mitad de la lista se acota al lado izquierdo solamente.
            return busca_d(lista, dato, ini, mitad - 1)    # Y se llama nuevamente a la función esta vez con la variable 'fin' solo hasta la mitad menos uno.
        else:    # Si el dato es mayor que el valor del medio se acota por el lado derecho.
            return busca_d(lista, dato, mitad + 1, fin)    # Y se llama a la función misma con la variable 'ini' desde la mitad mas uno.
    else:    # Si el dato no se encuentra en la lista se retorna la negación.
        return False

if busca_d(lista, dato, 0, n - 1):    # Se llama a la función de busqueda binaria con inicio en cero y fin en el total de elementos de la lista.
    # Si la función retorna True se encontro el dato en la lista.
    print("El dato", dato, "se encontró en la lista.")
else:    # Sino el dato no estaba en la lista ingresada.
    print("El dato", dato, "NO se encuentra en la lista.")
