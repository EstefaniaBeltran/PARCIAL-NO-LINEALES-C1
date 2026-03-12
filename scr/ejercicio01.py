"""
Módulo que implementa un árbol N-ario para modelar una estructura organizacional universitaria.
"""

from typing import Dict, Generator, Optional


class Nodo:
    """
    Representa un nodo dentro de un árbol N-ario.

    Attributes:
        nombre (str): Nombre del nodo.
        hijos (Dict[str, Nodo]): Diccionario de hijos indexados por nombre.
    """

    def __init__(self, nombre: str) -> None:
        """
        Inicializa un nodo con su nombre y sin hijos.

        Args:
            nombre: Nombre del nodo.
        """
        self.nombre: str = nombre
        self.hijos: Dict[str, "Nodo"] = {}  # Usamos dict para acceso O(1) por nombre

    def agregar_hijo(self, hijo: "Nodo") -> None:
        """
        Agrega un nodo hijo.

        Args:
            hijo: Nodo a agregar como hijo.
        """
        self.hijos[hijo.nombre] = hijo

    def recorrer(self) -> Generator[str, None, None]:
        """
        Recorre el árbol en profundidad (DFS) y genera los nombres de los nodos.

        Yields:
            El nombre del nodo actual y luego los de sus descendientes.
        """
        yield self.nombre
        for hijo in self.hijos.values():
            yield from hijo.recorrer()

    def __iter__(self):
        """Permite iterar sobre los hijos directamente (opcional, pero útil)."""
        return iter(self.hijos.values())


class ArbolNario:
    """
    Representa un árbol N-ario completo.

    Attributes:
        raiz (Nodo): Nodo raíz del árbol.
    """

    def __init__(self, raiz: Nodo) -> None:
        """
        Inicializa el árbol con una raíz.

        Args:
            raiz: Nodo raíz.
        """
        self.raiz = raiz

    def recorrer(self) -> Generator[str, None, None]:
        """
        Recorre el árbol en profundidad desde la raíz.

        Yields:
            Nombres de los nodos en orden DFS.
        """
        yield from self.raiz.recorrer()

    def __iter__(self):
        """Itera sobre los nodos en DFS (usa el generador)."""
        return self.recorrer()


def ejemplo_universidad() -> ArbolNario:
    """Construye y retorna un árbol de ejemplo de una universidad."""
    rectoria = Nodo("Rectoria")

    ingenieria = Nodo("Facultad Ingenieria")
    derecho = Nodo("Escuela Mayor de Derecho")
    prime = Nodo("PRIME")

    ingenieria.agregar_hijo(Nodo("Ciencia Computacion"))
    ingenieria.agregar_hijo(Nodo("Ingenieria Industrial"))
    ingenieria.agregar_hijo(Nodo("Ingenieria Ambiental"))

    derecho.agregar_hijo(Nodo("Derecho"))
    prime.agregar_hijo(Nodo("Negocios Internacionales"))

    rectoria.agregar_hijo(ingenieria)
    rectoria.agregar_hijo(derecho)
    rectoria.agregar_hijo(prime)

    return ArbolNario(rectoria)


if __name__ == "__main__":
    arbol = ejemplo_universidad()
    print("Recorrido del árbol:")
    for nodo in arbol.recorrer():
        print(nodo)
