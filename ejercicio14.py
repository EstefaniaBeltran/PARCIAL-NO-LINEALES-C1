"""
Módulo que implementa un planificador de tareas con prioridad.
Utiliza heapq y una clase Tarea con __lt__ sobrecargado.
"""

import heapq
from typing import List
from datetime import datetime


class Tarea:
    """Representa una tarea con prioridad y timestamp."""

    def __init__(self, prioridad: int, descripcion: str) -> None:
        self.prioridad = prioridad
        self.descripcion = descripcion
        self.timestamp = datetime.now()  # momento de creación

    def __lt__(self, other: "Tarea") -> bool:
        """
        Sobrecarga del operador < para que heapq pueda comparar tareas.
        Queremos que la tarea con mayor prioridad (número más bajo) sea la primera.
        En caso de igual prioridad, se ordena por timestamp (más antiguo primero).
        """
        if self.prioridad != other.prioridad:
            return self.prioridad < other.prioridad
        return self.timestamp < other.timestamp

    def __repr__(self) -> str:
        return f"Tarea(pri={self.prioridad}, desc='{self.descripcion}')"


class Planificador:
    """Cola de prioridad para tareas."""

    def __init__(self) -> None:
        self.cola: List[Tarea] = []

    def agregar_tarea(self, tarea: Tarea) -> None:
        """Añade una tarea a la cola."""
        heapq.heappush(self.cola, tarea)

    def ejecutar_tarea(self) -> Tarea:
        """Extrae y retorna la tarea de mayor prioridad."""
        if not self.cola:
            raise IndexError("No hay tareas pendientes")
        return heapq.heappop(self.cola)

    def tarea_pendiente(self) -> bool:
        return len(self.cola) > 0

    def __len__(self) -> int:
        return len(self.cola)


def ejemplo_planificador():
    plan = Planificador()
    plan.agregar_tarea(Tarea(1, "Actualizar sistema"))
    plan.agregar_tarea(Tarea(3, "Enviar correo"))
    plan.agregar_tarea(Tarea(2, "Respaldar datos"))

    print("Tareas en orden de prioridad:")
    while plan.tarea_pendiente():
        t = plan.ejecutar_tarea()
        print(t)

    # Probar igual prioridad
    plan.agregar_tarea(Tarea(2, "Tarea A"))
    import time
    time.sleep(0.1)
    plan.agregar_tarea(Tarea(2, "Tarea B"))
    print("\nTareas con misma prioridad (por timestamp):")
    while plan.tarea_pendiente():
        print(plan.ejecutar_tarea())


if __name__ == "__main__":
    ejemplo_planificador()