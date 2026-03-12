"""
Módulo que modela dependencias entre módulos de software.
"""

from typing import Dict, Generator, List, Set


class Modulo:
    """Representa un módulo de software con sus dependencias."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.dependencias: Dict[str, "Modulo"] = {}  # dependencias directas

    def agregar_dependencia(self, modulo: "Modulo") -> None:
        """Añade una dependencia directa."""
        self.dependencias[modulo.nombre] = modulo

    def obtener_todas_dependencias(self, visitados: Set[str] = None) -> Set[str]:
        """
        Retorna el conjunto de todos los módulos de los que depende (directa o indirectamente).
        Útil para analizar impacto de cambios.
        """
        if visitados is None:
            visitados = set()
        if self.nombre in visitados:
            return visitados
        visitados.add(self.nombre)
        for dep in self.dependencias.values():
            dep.obtener_todas_dependencias(visitados)
        return visitados

    def __repr__(self) -> str:
        return f"Modulo({self.nombre})"


class SistemaModulos:
    """Sistema que contiene un módulo raíz y sus dependencias."""

    def __init__(self, raiz: Modulo) -> None:
        self.raiz = raiz

    def impacto_cambio(self, modulo_afectado: str) -> Set[str]:
        """
        Determina qué módulos se verían afectados si se cambia 'modulo_afectado'.
        (Búsqueda inversa: quiénes dependen de él). Por simplicidad, no implementada.
        """
        # Requeriría tener referencias a los padres o un grafo completo.
        return set()


def ejemplo_dependencias() -> SistemaModulos:
    """Construye un sistema de ejemplo con dependencias."""
    sistema = Modulo("Sistema")
    modulo_a = Modulo("ModuloA")
    modulo_b = Modulo("ModuloB")

    lib1 = Modulo("Libreria1")
    lib2 = Modulo("Libreria2")
    lib3 = Modulo("Libreria3")

    modulo_a.agregar_dependencia(lib1)
    modulo_a.agregar_dependencia(lib2)
    modulo_b.agregar_dependencia(lib3)

    sistema.agregar_dependencia(modulo_a)
    sistema.agregar_dependencia(modulo_b)

    return SistemaModulos(sistema)


if __name__ == "__main__":
    sistema = ejemplo_dependencias()
    print("Dependencias totales del sistema:")
    print(sistema.raiz.obtener_todas_dependencias())