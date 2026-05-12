class Aula:
    _nombre: str = ""

    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nom: str):
        self._nombre = nuevo_nom
