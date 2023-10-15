class nodoPila():
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Pila():
    def __init__(self):
        self.primero = None
    
    def apilar(self, valor):
        nuevo = nodoPila(valor, self.primero)
        self.primero = nuevo

    def desapilar(self):
        if self.primero is None:
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        return valor

    def estaVacia(self):
        return self.primero is None

    def __str__(self):
        aux = self.primero
        elementos = []
        while aux:
            elementos.append(str(aux.valor))
            aux = aux.siguiente
        return ", ".join(elementos)
