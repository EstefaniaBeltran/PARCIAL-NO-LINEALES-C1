"""
Módulo que implementa un Trie para autocompletado.
"""

from typing import Dict, Generator, List, Optional


class NodoTrie:
    """Nodo de un Trie."""

    def __init__(self) -> None:
        self.hijos: Dict[str, "NodoTrie"] = {}
        self.fin_palabra: bool = False


class Trie:
    """Trie para almacenar palabras y generar sugerencias por prefijo."""

    def __init__(self) -> None:
        self.raiz = NodoTrie()

    def insertar(self, palabra: str) -> None:
        """Inserta una palabra en el Trie."""
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = NodoTrie()
            nodo = nodo.hijos[letra]
        nodo.fin_palabra = True

    def buscar(self, palabra: str) -> bool:
        """Verifica si una palabra exacta está en el Trie."""
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                return False
            nodo = nodo.hijos[letra]
        return nodo.fin_palabra

    def _encontrar_nodo(self, prefijo: str) -> Optional[NodoTrie]:
        """Retorna el nodo al final del prefijo, o None si no existe."""
        nodo = self.raiz
        for letra in prefijo:
            if letra not in nodo.hijos:
                return None
            nodo = nodo.hijos[letra]
        return nodo

    def sugerir(self, prefijo: str) -> Generator[str, None, None]:
        """
        Genera todas las palabras que comienzan con el prefijo dado.

        Args:
            prefijo: Prefijo a buscar.

        Yields:
            Cada palabra completa que tiene ese prefijo.
        """
        nodo = self._encontrar_nodo(prefijo)
        if nodo is None:
            return

        # Realizamos DFS desde el nodo para recolectar palabras
        pila = [(nodo, prefijo)]
        while pila:
            actual, palabra_parcial = pila.pop()
            if actual.fin_palabra:
                yield palabra_parcial
            # Iteramos sobre los hijos en orden (para consistencia)
            for letra in sorted(actual.hijos.keys()):
                pila.append((actual.hijos[letra], palabra_parcial + letra))


def ejemplo_trie():
    trie = Trie()
    palabras = ["casa", "carro", "carta", "perro", "gato"]
    for p in palabras:
        trie.insertar(p)

    print("Buscar 'casa':", trie.buscar("casa"))
    print("Buscar 'casa' (debe ser True)")
    print("Buscar 'cama':", trie.buscar("cama"))

    print("\nSugerencias para 'ca':")
    for palabra in trie.sugerir("ca"):
        print(palabra)


if __name__ == "__main__":
    ejemplo_trie()