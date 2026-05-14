import datetime

class Guardia:
    _id: str = ""
    _dia = datetime.date
    _hora: str = ""
    _curso: str = ""
    _clase: str = ""
    _tarea: str = ""
    _ficheros: str = ""

    def __init__(self, id, dia, hora, curso, clase, tarea, ficheros: str = ""):
        self._id = id
        self._dia = dia
        self._hora = hora
        self._curso = curso
        self._clase = clase
        self._tarea = tarea
        self._ficheros = ficheros

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id: str):
        self._id = nuevo_id

    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, nuevo_dia: str):
        self._dia = nuevo_dia

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, nuevo_hora: str):
        self._hora = nuevo_hora

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, nuevo_curso: str):
        self._curso = nuevo_curso

    @property
    def clase(self):
        return self._clase

    @clase.setter
    def clase(self, nuevo_clase: str):
        self._clase = nuevo_clase

    @property
    def tarea(self):
        return self._tarea

    @tarea.setter
    def tarea(self, nuevo_tarea: str):
        self._tarea = nuevo_tarea

    @property
    def ficheros(self):
        return self._ficheros

    @ficheros.setter
    def ficheros(self, nuevo_ficheros: str):
        self._ficheros = nuevo_ficheros
