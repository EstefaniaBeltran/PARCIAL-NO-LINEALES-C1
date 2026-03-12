"""
Módulo que implementa un árbol de decisión simple para clasificar intenciones.
"""

from typing import Optional, Dict, Any


class NodoDecision:
    """Nodo de un árbol de decisión."""

    def __init__(self, pregunta: str, opciones: Dict[str, Any] = None):
        """
        Args:
            pregunta: La pregunta o condición.
            opciones: Diccionario que mapea respuestas a subárboles o resultados.
        """
        self.pregunta = pregunta
        self.opciones: Dict[str, Any] = opciones if opciones is not None else {}

    def decidir(self, respuesta: str) -> Any:
        """Toma una decisión basada en la respuesta dada."""
        return self.opciones.get(respuesta, None)


class ArbolDecision:
    """Árbol de decisión con un nodo raíz."""

    def __init__(self, raiz: NodoDecision) -> None:
        self.raiz = raiz

    def evaluar(self, respuestas: Dict[str, str]) -> Optional[str]:
        """
        Evalúa el árbol siguiendo las respuestas del usuario.

        Args:
            respuestas: Diccionario con las respuestas a las preguntas (pregunta -> respuesta).

        Returns:
            La decisión final o None si no se llega a una hoja.
        """
        nodo = self.raiz
        while True:
            if nodo.pregunta in respuestas:
                sig = nodo.decidir(respuestas[nodo.pregunta])
                if isinstance(sig, NodoDecision):
                    nodo = sig
                else:
                    return sig  # es una hoja (resultado)
            else:
                # No hay respuesta para esta pregunta
                return None


def ejemplo_decision() -> ArbolDecision:
    """Construye un árbol de decisión de ejemplo."""
    # Nodo raíz
    raiz = NodoDecision("¿Está lloviendo?")

    # Subárboles
    si_llueve = NodoDecision("Llevar paraguas", {"si": "Llevar paraguas", "no": "No llevar paraguas"})
    no_llueve = NodoDecision("No llevar paraguas", {"si": "No llevar paraguas"})

    # Conectar opciones
    raiz.opciones["si"] = si_llueve
    raiz.opciones["no"] = no_llueve

    return ArbolDecision(raiz)


if __name__ == "__main__":
    arbol = ejemplo_decision()
    respuestas = {"¿Está lloviendo?": "si", "Llevar paraguas": "si"}
    resultado = arbol.evaluar(respuestas)
    print(f"Decisión: {resultado}")