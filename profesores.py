class Profesor:
    _id: str = ""
    _nombre: str = ""
    _apellido: str = ""
    _clave: str = ""

    def __init__(self, id, nombre, apellido, clave):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._clave = clave

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id: str):
        self._id = nuevo_id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nom: str):
        self._nombre = nuevo_nom

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido: str):
        self._apellido = nuevo_apellido

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, nuevo_clave: str):
        self._clave = nuevo_clave
