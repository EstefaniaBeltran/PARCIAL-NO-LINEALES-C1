"""
Módulo que implementa un motor de búsqueda simple con autocompletado y priorización.
Usa un Trie para almacenar términos y un heap para ordenar sugerencias por relevancia.
"""

import heapq
from typing import Dict, Generator, List, Tuple, Optional


class NodoTrie:
    def __init__(self) -> None:
        self.hijos: Dict[str, "NodoTrie"] = {}
        self.fin: bool = False
        self.relevancia: int = 0  # podría ser número de búsquedas, etc.


class MotorBusqueda:
    """Motor de búsqueda con autocompletado y priorización."""

    def __init__(self) -> None:
        self.raiz = NodoTrie()

    def insertar(self, termino: str, relevancia: int = 1) -> None:
        """
        Inserta un término con una relevancia inicial.
        Si ya existe, se suma la relevancia.
        """
        nodo = self.raiz
        for letra in termino:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = NodoTrie()
            nodo = nodo.hijos[letra]
        nodo.fin = True
        nodo.relevancia += relevancia

    def _encontrar_nodo(self, prefijo: str) -> Optional[NodoTrie]:
        nodo = self.raiz
        for letra in prefijo:
            if letra not in nodo.hijos:
                return None
            nodo = nodo.hijos[letra]
        return nodo

    def sugerir(self, prefijo: str) -> Generator[Tuple[int, str], None, None]:
        """
        Genera sugerencias para el prefijo, ordenadas por relevancia (mayor primero).
        Usa un heap para priorizar.
        """
        nodo = self._encontrar_nodo(prefijo)
        if not nodo:
            return

        # Realizamos DFS y guardamos en una lista de ( -relevancia, palabra ) para heap máximo
        heap: List[Tuple[int, str]] = []
        pila = [(nodo, prefijo)]
        while pila:
            actual, palabra_parcial = pila.pop()
            if actual.fin:
                # Usamos relevancia negativa para simular max-heap con heapq (que es min-heap)
                heapq.heappush(heap, (-actual.relevancia, palabra_parcial))
            for letra, hijo in actual.hijos.items():
                pila.append((hijo, palabra_parcial + letra))

        # Extraemos del heap en orden
        while heap:
            neg_rel, palabra = heapq.heappop(heap)
            yield (-neg_rel, palabra)  # devolvemos relevancia positiva

    def buscar(self, termino: str) -> bool:
        """Verifica si existe el término exacto."""
        nodo = self._encontrar_nodo(termino)
        return nodo is not None and nodo.fin

    # Podríamos añadir un método para incrementar relevancia al buscar
    def incrementar_relevancia(self, termino: str) -> None:
        """Incrementa la relevancia de un término (simula que se busca)."""
        nodo = self._encontrar_nodo(termino)
        if nodo and nodo.fin:
            nodo.relevancia += 1


def ejemplo_motor():
    motor = MotorBusqueda()
    # Insertar algunos títulos académicos con relevancia inicial
    motor.insertar("Ciencia de la Computación", 10)
    motor.insertar("Ciencias de la Educación", 5)
    motor.insertar("Ciencia de Datos", 8)
    motor.insertar("Arquitectura de Computadores", 3)

    print("Sugerencias para 'Ciencia':")
    for relevancia, palabra in motor.sugerir("Ciencia"):
        print(f"{palabra} (relevancia {relevancia})")

    # Simular búsqueda que aumenta relevancia
    motor.incrementar_relevancia("Ciencia de Datos")
    print("\nDespués de buscar 'Ciencia de Datos', las sugerencias cambian:")
    for relevancia, palabra in motor.sugerir("Ciencia"):
        print(f"{palabra} (relevancia {relevancia})")


if __name__ == "__main__":
    ejemplo_motor()