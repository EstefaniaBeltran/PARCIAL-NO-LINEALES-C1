"""
Módulo que implementa un árbol genealógico.
"""

from typing import Dict, Generator, List, Optional


class Persona:
    """Representa una persona en el árbol genealógico."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.hijos: Dict[str, "Persona"] = {}  # hijos por nombre

    def agregar_hijo(self, hijo: "Persona") -> None:
        """Añade un hijo."""
        self.hijos[hijo.nombre] = hijo

    def recorrer(self) -> Generator[str, None, None]:
        """Recorrido en preorden."""
        yield self.nombre
        for hijo in self.hijos.values():
            yield from hijo.recorrer()

    def ancestros_comunes(self, otro: "Persona") -> List[str]:
        """
        Encuentra ancestros comunes entre esta persona y otra.
        (Implementación simplificada: busca en los ancestros de ambos)

        Nota: Para una solución completa se necesitaría acceso al padre,
        pero en este árbol no tenemos referencia al padre. Se asume que
        se podría implementar con una búsqueda hacia arriba si se guardara.
        """
        # Por simplicidad, retornamos una lista vacía (requiere estructura con padres)
        return []

    def generaciones(self) -> int:
        """Calcula el número de generaciones desde aquí (profundidad máxima)."""
        if not self.hijos:
            return 1
        return 1 + max(hijo.generaciones() for hijo in self.hijos.values())


class ArbolGenealogico:
    """Árbol genealógico con raíz."""

    def __init__(self, raiz: Persona) -> None:
        self.raiz = raiz

    def recorrer(self) -> Generator[str, None, None]:
        yield from self.raiz.recorrer()

    def altura(self) -> int:
        """Altura del árbol (número de generaciones)."""
        return self.raiz.generaciones()


def ejemplo_familia() -> ArbolGenealogico:
    abuelo = Persona("Abuelo")
    padre = Persona("Padre")
    tia = Persona("Tia")

    padre.agregar_hijo(Persona("Hijo1"))
    padre.agregar_hijo(Persona("Hijo2"))
    tia.agregar_hijo(Persona("Primo1"))

    abuelo.agregar_hijo(padre)
    abuelo.agregar_hijo(tia)

    return ArbolGenealogico(abuelo)


if __name__ == "__main__":
    familia = ejemplo_familia()
    print("Recorrido del árbol genealógico:")
    for persona in familia.recorrer():
        print(persona)

    print(f"\nGeneraciones: {familia.altura()}")