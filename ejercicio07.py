"""
Módulo que implementa un corrector ortográfico basado en Trie.
"""

from typing import List
# Reutilizamos la clase Trie del ejercicio6 (podría estar en otro archivo, pero aquí la incluimos)
# Para mantener independencia, copiamos la implementación del Trie (simplificada)

class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.fin_palabra = False


class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, palabra: str) -> None:
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = NodoTrie()
            nodo = nodo.hijos[letra]
        nodo.fin_palabra = True

    def buscar(self, palabra: str) -> bool:
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                return False
            nodo = nodo.hijos[letra]
        return nodo.fin_palabra


class CorrectorOrtografico:
    """Corrector que usa un Trie como diccionario."""

    def __init__(self, trie: Trie) -> None:
        self.trie = trie

    def cargar_palabras(self, palabras: List[str]) -> None:
        """Carga una lista de palabras en el Trie."""
        for palabra in palabras:
            self.trie.insertar(palabra)

    def verificar(self, palabra: str) -> bool:
        """Retorna True si la palabra está en el diccionario."""
        return self.trie.buscar(palabra)

    # Se podría añadir un método para sugerir correcciones (opcional)
    # def sugerir_correcciones(self, palabra: str) -> List[str]:
    #     ...


def ejemplo_corrector():
    trie = Trie()
    corrector = CorrectorOrtografico(trie)
    palabras = ["hola", "mundo", "python"]
    corrector.cargar_palabras(palabras)

    print(corrector.verificar("hola"))   # True
    print(corrector.verificar("java"))   # False


if __name__ == "__main__":
    ejemplo_corrector()