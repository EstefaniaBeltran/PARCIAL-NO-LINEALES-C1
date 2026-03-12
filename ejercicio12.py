"""
Módulo que compara el rendimiento de una tabla hash y un Trie para búsqueda de palabras.
"""

import time
import random
import string
from typing import List, Callable


# --- Implementación de Tabla Hash (para cadenas) ---
class HashTableStr:
    def __init__(self, size=1000):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key: str) -> int:
        # Función hash simple para strings
        return sum(ord(c) for c in key) % self.size

    def insert(self, key: str) -> None:
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key: str) -> bool:
        index = self._hash(key)
        return key in self.table[index]


# --- Implementación de Trie ---
class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.fin = False


class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def insert(self, palabra: str) -> None:
        nodo = self.raiz
        for c in palabra:
            if c not in nodo.hijos:
                nodo.hijos[c] = NodoTrie()
            nodo = nodo.hijos[c]
        nodo.fin = True

    def search(self, palabra: str) -> bool:
        nodo = self.raiz
        for c in palabra:
            if c not in nodo.hijos:
                return False
            nodo = nodo.hijos[c]
        return nodo.fin


def generar_palabras(cantidad: int, longitud: int = 5) -> List[str]:
    """Genera palabras aleatorias."""
    palabras = []
    for _ in range(cantidad):
        palabra = ''.join(random.choices(string.ascii_lowercase, k=longitud))
        palabras.append(palabra)
    return palabras


def medir_tiempo(estructura, inserciones: List[str], busquedas: List[str],
                 insert_func: Callable, search_func: Callable) -> float:
    """Mide el tiempo de búsqueda después de insertar."""
    for palabra in inserciones:
        insert_func(estructura, palabra)
    inicio = time.perf_counter()
    for palabra in busquedas:
        search_func(estructura, palabra)
    fin = time.perf_counter()
    return fin - inicio


def comparar():
    print("Comparación Hash vs Trie")
    print("-" * 40)

    # Conjuntos de datos
    palabras_insertar = generar_palabras(5000, 6)
    palabras_buscar = random.sample(palabras_insertar, 1000) + generar_palabras(500, 6)  # mezcla existentes y no existentes

    # Hash
    hash_tabla = HashTableStr(size=2000)
    tiempo_hash = medir_tiempo(
        hash_tabla, palabras_insertar, palabras_buscar,
        lambda ht, p: ht.insert(p),
        lambda ht, p: ht.search(p)
    )
    print(f"Tiempo de búsqueda con Hash: {tiempo_hash:.6f} segundos")

    # Trie
    trie = Trie()
    tiempo_trie = medir_tiempo(
        trie, palabras_insertar, palabras_buscar,
        lambda t, p: t.insert(p),
        lambda t, p: t.search(p)
    )
    print(f"Tiempo de búsqueda con Trie: {tiempo_trie:.6f} segundos")

    # Comparación de memoria aproximada (solo estimación)
    import sys
    mem_hash = sys.getsizeof(hash_tabla) + sum(sys.getsizeof(b) for b in hash_tabla.table)
    mem_trie = sys.getsizeof(trie)  # No es precisa, pero da una idea
    print(f"\nMemoria aproximada (solo objeto principal): Hash {mem_hash} bytes, Trie {mem_trie} bytes")


if __name__ == "__main__":
    comparar()