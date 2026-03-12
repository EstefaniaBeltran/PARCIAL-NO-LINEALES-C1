"""
Módulo que simula una red donde los paquetes tienen prioridad.
Utiliza una cola de prioridad con heapq.
"""

import heapq
from typing import List, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Paquete:
    """Representa un paquete de red con prioridad y timestamp."""
    prioridad: int      # menor número = mayor prioridad
    contenido: str
    timestamp: datetime = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

    def __lt__(self, other: "Paquete") -> bool:
        """Comparación para heapq: primero por prioridad, luego por timestamp."""
        if self.prioridad != other.prioridad:
            return self.prioridad < other.prioridad
        return self.timestamp < other.timestamp

    def __repr__(self) -> str:
        return f"Paquete(pri={self.prioridad}, cont='{self.contenido}')"


class Red:
    """Simula una red con cola de prioridad de paquetes."""

    def __init__(self) -> None:
        self.cola: List[Paquete] = []

    def enviar_paquete(self, paquete: Paquete) -> None:
        """Agrega un paquete a la red."""
        heapq.heappush(self.cola, paquete)

    def procesar_paquete(self) -> Paquete:
        """Procesa el paquete de mayor prioridad."""
        if not self.cola:
            raise IndexError("No hay paquetes en la red")
        return heapq.heappop(self.cola)

    def paquetes_pendientes(self) -> int:
        return len(self.cola)


def ejemplo_red():
    red = Red()
    red.enviar_paquete(Paquete(1, "Video en tiempo real"))
    red.enviar_paquete(Paquete(3, "Correo electrónico"))
    red.enviar_paquete(Paquete(2, "Mensaje de chat"))

    print("Procesando paquetes en orden de prioridad:")
    while red.paquetes_pendientes() > 0:
        paq = red.procesar_paquete()
        print(paq)

    # Prueba con igual prioridad
    red.enviar_paquete(Paquete(2, "Paquete A"))
    import time
    time.sleep(0.1)
    red.enviar_paquete(Paquete(2, "Paquete B"))
    print("\nPaquetes con misma prioridad (por timestamp):")
    while red.paquetes_pendientes():
        print(red.procesar_paquete())


if __name__ == "__main__":
    ejemplo_red()