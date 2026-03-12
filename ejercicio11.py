"""
Módulo que implementa una tabla hash para registro de estudiantes.
Maneja colisiones mediante encadenamiento (listas).
"""

from typing import List, Tuple, Optional, Iterator


class HashTable:
    """Tabla hash con direccionamiento abierto mediante listas."""

    def __init__(self, size: int = 10) -> None:
        """
        Args:
            size: Tamaño inicial de la tabla.
        """
        self.size = size
        self.table: List[List[Tuple[int, str]]] = [[] for _ in range(size)]
        self._num_elementos = 0

    def _hash(self, key: int) -> int:
        """Función hash simple: módulo del tamaño."""
        return key % self.size

    def __setitem__(self, key: int, value: str) -> None:
        """Inserta o actualiza un estudiante con la sintaxis tabla[key] = value."""
        index = self._hash(key)
        bucket = self.table[index]
        # Buscar si ya existe la clave para actualizar
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # Si no existe, agregar nueva entrada
        bucket.append((key, value))
        self._num_elementos += 1
        # Opcional: verificar factor de carga y redimensionar
        # if self._num_elementos / self.size > 0.75:
        #     self._redimensionar()

    def __getitem__(self, key: int) -> str:
        """Obtiene el valor asociado a la clave. Lanza KeyError si no existe."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(f"ID {key} no encontrado")

    def get(self, key: int) -> Optional[str]:
        """Versión segura que retorna None si no existe."""
        try:
            return self[key]
        except KeyError:
            return None

    def __delitem__(self, key: int) -> None:
        """Elimina un elemento por su clave."""
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._num_elementos -= 1
                return
        raise KeyError(f"ID {key} no encontrado")

    def __iter__(self) -> Iterator[Tuple[int, str]]:
        """Itera sobre todos los pares (clave, valor) en la tabla."""
        for bucket in self.table:
            for item in bucket:
                yield item

    def __len__(self) -> int:
        return self._num_elementos

    def factor_carga(self) -> float:
        """Retorna el factor de carga actual."""
        return self._num_elementos / self.size


def ejemplo_hash():
    tabla = HashTable()
    tabla[101] = "Ana"
    tabla[102] = "Luis"
    tabla[103] = "Carlos"
    # También se podría usar insert como método, pero usamos la sintaxis de item

    print(tabla[102])  # Luis
    print(tabla.get(104))  # None

    print("\nTodos los estudiantes:")
    for id_, nombre in tabla:
        print(f"ID: {id_}, Nombre: {nombre}")

    print(f"\nFactor de carga: {tabla.factor_carga():.2f}")

    # Prueba de eliminación
    del tabla[102]
    print("\nDespués de eliminar ID 102:")
    for id_, nombre in tabla:
        print(f"ID: {id_}, Nombre: {nombre}")


if __name__ == "__main__":
    ejemplo_hash()