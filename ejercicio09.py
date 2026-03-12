"""
Módulo que implementa un diccionario multilenguaje usando un Trie.
Cada nodo puede tener significados en varios idiomas.
"""

from typing import Dict, Generator, List, Optional


class NodoTrieMultilenguaje:
    """Nodo de Trie que puede contener significados en varios idiomas."""

    def __init__(self) -> None:
        self.hijos: Dict[str, "NodoTrieMultilenguaje"] = {}
        self.significados: Dict[str, str] = {}  # idioma -> definición


class DiccionarioMultilenguaje:
    """
    Diccionario que permite insertar palabras con su significado en varios idiomas.
    Basado en Trie para búsqueda rápida por prefijo.
    """

    def __init__(self) -> None:
        self.raiz = NodoTrieMultilenguaje()

    def insertar(self, palabra: str, idioma: str, significado: str) -> None:
        """
        Inserta una palabra en un idioma con su significado.

        Args:
            palabra: La palabra a insertar.
            idioma: Código del idioma (ej. 'es', 'en').
            significado: Definición en ese idioma.
        """
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = NodoTrieMultilenguaje()
            nodo = nodo.hijos[letra]
        nodo.significados[idioma] = significado

    def buscar(self, palabra: str, idioma: Optional[str] = None) -> Dict[str, str] | str | None:
        """
        Busca una palabra.

        Args:
            palabra: Palabra a buscar.
            idioma: Si se especifica, retorna solo el significado en ese idioma (o None si no existe).

        Returns:
            Si idioma es None: diccionario con todos los significados (idioma -> definición).
            Si idioma se especifica: la definición en ese idioma o None.
            Si la palabra no existe: None.
        """
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                return None
            nodo = nodo.hijos[letra]

        if idioma:
            return nodo.significados.get(idioma)
        return nodo.significados if nodo.significados else None

    def sugerir(self, prefijo: str) -> Generator[str, None, None]:
        """Sugiere palabras que comienzan con el prefijo (sin importar idioma)."""
        nodo = self.raiz
        for letra in prefijo:
            if letra not in nodo.hijos:
                return
            nodo = nodo.hijos[letra]

        # DFS para recolectar palabras
        pila = [(nodo, prefijo)]
        while pila:
            actual, palabra_parcial = pila.pop()
            if actual.significados:
                yield palabra_parcial
            for letra in sorted(actual.hijos.keys()):
                pila.append((actual.hijos[letra], palabra_parcial + letra))


def ejemplo_diccionario():
    dic = DiccionarioMultilenguaje()
    dic.insertar("casa", "es", "edificio para habitar")
    dic.insertar("casa", "en", "house")
    dic.insertar("cat", "en", "animal")
    dic.insertar("gato", "es", "animal doméstico")

    print("Buscar 'casa' en español:", dic.buscar("casa", "es"))
    print("Buscar 'casa' en inglés:", dic.buscar("casa", "en"))
    print("Todos los significados de 'casa':", dic.buscar("casa"))

    print("\nSugerencias para 'ca':")
    for palabra in dic.sugerir("ca"):
        print(palabra)


if __name__ == "__main__":
    ejemplo_diccionario()