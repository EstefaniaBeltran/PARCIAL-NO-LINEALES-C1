"""
Módulo que implementa un heap mínimo utilizando heapq.
"""

import heapq
from typing import List, Iterator


class MinHeap:
    """Heap mínimo utilizando la biblioteca heapq."""

    def __init__(self) -> None:
        self.heap: List[int] = []

    def insert(self, value: int) -> None:
        """Inserta un elemento en el heap."""
        heapq.heappush(self.heap, value)

    def extract_min(self) -> int:
        """Extrae y retorna el elemento mínimo."""
        if not self.heap:
            raise IndexError("El heap está vacío")
        return heapq.heappop(self.heap)

    def __iter__(self) -> Iterator[int]:
        """Permite iterar sobre los elementos (sin orden garantizado)."""
        return iter(self.heap)

    def __len__(self) -> int:
        return len(self.heap)

    def peek(self) -> int:
        """Retorna el mínimo sin extraerlo."""
        if not self.heap:
            raise IndexError("Heap vacío")
        return self.heap[0]


def probar_heap():
    heap = MinHeap()
    valores = [10, 4, 15, 2, 8]
    for v in valores:
        heap.insert(v)

    print("Elementos en el heap:", list(heap))
    print("Mínimo:", heap.extract_min())
    print("Nuevo mínimo después de extraer:", heap.peek())
    print("Heap restante:", list(heap))

    # Caso límite: extraer todos
    print("\nExtrayendo todos:")
    while heap:
        print(heap.extract_min(), end=" ")
    print()

    # Intentar extraer de heap vacío (lanzará excepción)
    try:
        heap.extract_min()
    except IndexError as e:
        print(f"Error esperado: {e}")


if __name__ == "__main__":
    probar_heap()