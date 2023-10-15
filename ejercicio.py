from pila2 import *
def getTablero(n):
    torre1 = Pila()
    for i in range(n, 0, -1):
        torre1.apilar(i)
    torre2 = Pila()
    torre3 = Pila()
    return torre1, torre2, torre3

def solve(tablero, disco, origen, destino, auxiliar, movimientos):
    if disco == 1:
        movimientos.append(f'D{disco} from T{origen} to T{destino}')
        destino.apilar(origen.desapilar())
    else:
        solve(tablero, disco - 1, origen, auxiliar, destino, movimientos)
        movimientos.append(f'D{disco} from T{origen} to T{destino}')
        destino.apilar(origen.desapilar())
        solve(tablero, disco - 1, auxiliar, destino, origen, movimientos)

# Inicializar el tablero con 3 discos
torre1, torre2, torre3 = getTablero(3)
tablero = [torre1, torre2, torre3]

# Resolver el problema y obtener la lista de movimientos
movimientos = []
solve(tablero, 3, torre1, torre3, torre2, movimientos)

# Mostrar la lista de movimientos
print("Lista de movimientos:")
for movimiento in movimientos:
    print(movimiento)

# Mostrar contenido final de las pilas
print("\nContenido final de las pilas:")
for i, torre in enumerate(tablero):
    print(f'Torre {i + 1}: {torre}')
