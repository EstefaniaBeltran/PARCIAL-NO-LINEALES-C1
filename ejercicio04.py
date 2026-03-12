"""
Módulo que modela un menú jerárquico de aplicación.
"""

from typing import Dict, Generator, List, Optional


class NodoMenu:
    """Nodo que representa una opción de menú."""

    def __init__(self, opcion: str) -> None:
        self.opcion = opcion
        self.submenus: Dict[str, "NodoMenu"] = {}

    def agregar(self, nodo: "NodoMenu") -> None:
        """Agrega una subopción."""
        self.submenus[nodo.opcion] = nodo

    def recorrer(self, nivel: int = 0) -> Generator[str, None, None]:
        """Recorre el menú mostrando la jerarquía."""
        yield "  " * nivel + self.opcion
        for sub in self.submenus.values():
            yield from sub.recorrer(nivel + 1)

    def contar_por_nivel(self, nivel_actual: int, contador: Dict[int, int]) -> None:
        """Cuenta cuántos nodos hay en cada nivel."""
        contador[nivel_actual] = contador.get(nivel_actual, 0) + 1
        for sub in self.submenus.values():
            sub.contar_por_nivel(nivel_actual + 1, contador)


class Menu:
    """Menú completo con raíz."""

    def __init__(self, raiz: NodoMenu) -> None:
        self.raiz = raiz

    def mostrar(self) -> None:
        """Muestra el menú por consola."""
        for linea in self.raiz.recorrer():
            print(linea)

    def contar_nodos_por_nivel(self) -> Dict[int, int]:
        """Retorna un diccionario con la cantidad de nodos por nivel."""
        contador: Dict[int, int] = {}
        self.raiz.contar_por_nivel(0, contador)
        return contador


def ejemplo_menu() -> Menu:
    """Crea un menú de ejemplo."""
    menu_principal = NodoMenu("Menú Principal")
    archivo = NodoMenu("Archivo")
    editar = NodoMenu("Editar")

    archivo.agregar(NodoMenu("Nuevo"))
    archivo.agregar(NodoMenu("Guardar"))
    editar.agregar(NodoMenu("Copiar"))
    editar.agregar(NodoMenu("Pegar"))

    menu_principal.agregar(archivo)
    menu_principal.agregar(editar)

    return Menu(menu_principal)


if __name__ == "__main__":
    menu = ejemplo_menu()
    menu.mostrar()
    print("\nConteo por niveles:")
    for nivel, cantidad in menu.contar_nodos_por_nivel().items():
        print(f"Nivel {nivel}: {cantidad} nodos")