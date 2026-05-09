import hashlib


class Profesor:
    _id: str = ""
    _nombre: str = ""
    _apellido: str = ""
    _clave: str = ""

    def __init__(self, id, nombre, apellido, clave):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._clave = self.encriptar_clave(clave)

    def __str__(self):
        return f"{self._nombre} {self._apellido}: ID {self._id} clave {self._clave}"

    def encriptar_clave(self, nueva_clave: str) -> str:
        """
        Recoge la clave introducida y la encripta con la forma SHA-1,
        para no guardar los datos sensibles de forma explícita.

        :param nueva_clave:
        :return:
        """
        texto_a_bytes = nueva_clave.encode('utf-8')
        clave_sha1_obj = hashlib.sha1(texto_a_bytes)
        clave_encriptada = clave_sha1_obj.hexdigest()
        return clave_encriptada

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

    @clave.setter
    def clave(self, nueva_clave: str):
        self._clave = self.encriptar_clave(nueva_clave)
