"""
Módulo que simula un sistema de archivos mediante un árbol N-ario.
"""

from typing import Dict, Generator, Optional


class NodoArchivo:
    """
    Representa un elemento del sistema de archivos (carpeta o archivo).

    Attributes:
        nombre (str): Nombre del elemento.
        hijos (Dict[str, NodoArchivo]): Si es carpeta, contiene los hijos; si es archivo, estará vacío.
    """

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.hijos: Dict[str, "NodoArchivo"] = {}

    def agregar(self, nodo: "NodoArchivo") -> None:
        """Agrega un hijo (solo si es carpeta)."""
        self.hijos[nodo.nombre] = nodo

    def recorrer(self) -> Generator[str, None, None]:
        """Recorre el árbol en profundidad."""
        yield self.nombre
        for hijo in self.hijos.values():
            yield from hijo.recorrer()

    def buscar(self, nombre: str) -> Optional["NodoArchivo"]:
        """
        Busca un nodo por nombre en el subárbol.

        Args:
            nombre: Nombre del archivo o carpeta a buscar.

        Returns:
            El nodo si se encuentra, None en caso contrario.
        """
        if self.nombre == nombre:
            return self
        for hijo in self.hijos.values():
            resultado = hijo.buscar(nombre)
            if resultado:
                return resultado
        return None

    def eliminar(self, nombre: str) -> bool:
        """
        Elimina un hijo por nombre (borrado recursivo).

        Args:
            nombre: Nombre del elemento a eliminar.

        Returns:
            True si se eliminó, False si no se encontró.
        """
        if nombre in self.hijos:
            del self.hijos[nombre]
            return True
        for hijo in self.hijos.values():
            if hijo.eliminar(nombre):
                return True
        return False


class SistemaArchivos:
    """Sistema de archivos con un nodo raíz."""

    def __init__(self, raiz: NodoArchivo) -> None:
        self.raiz = raiz

    def recorrer(self) -> Generator[str, None, None]:
        yield from self.raiz.recorrer()

    def buscar(self, nombre: str) -> Optional[NodoArchivo]:
        return self.raiz.buscar(nombre)

    def eliminar(self, nombre: str) -> bool:
        return self.raiz.eliminar(nombre)


def ejemplo_sistema_archivos() -> SistemaArchivos:
    """Crea un sistema de archivos de ejemplo."""
    raiz = NodoArchivo("sistema_archivos")  # snake_case recomendado

    docs = NodoArchivo("documentos")
    imgs = NodoArchivo("imagenes")

    docs.agregar(NodoArchivo("tarea.docx"))
    docs.agregar(NodoArchivo("tesis.pdf"))

    imgs.agregar(NodoArchivo("foto1.png"))
    imgs.agregar(NodoArchivo("foto2.png"))

    raiz.agregar(docs)
    raiz.agregar(imgs)

    return SistemaArchivos(raiz)


if __name__ == "__main__":
    sistema = ejemplo_sistema_archivos()
    print("Contenido del sistema:")
    for archivo in sistema.recorrer():
        print(archivo)

    # Prueba de búsqueda
    encontrado = sistema.buscar("tesis.pdf")
    print(f"\n¿Se encontró tesis.pdf? {encontrado is not None}")

    # Prueba de eliminación
    sistema.eliminar("foto1.png")
    print("\nDespués de eliminar foto1.png:")
    for archivo in sistema.recorrer():
        print(archivo)