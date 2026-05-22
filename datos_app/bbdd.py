import mysql
from mysql.connector import errorcode
from ficheros.config import Config


class BaseDatos:
    CONEXION = Config.cnx
    PROF = Config.PROF_TXT

    def cargar_profesores(self):
        cursor = self.CONEXION.cursor()
        self.CONEXION.autocommit = True
        recoger_prof = "SELECT * FROM profesores where apellidos != 'ADMIN'"
        try:
            cursor.execute(recoger_prof)
            for id, nombre, apellidos, clave in cursor:
                with open(self.PROF, 'a', encoding='utf-8') as f:
                    f.write(id + "," + nombre + "," + apellidos + "," + clave + "\n")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de conexión.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe dicha base de datos.")
            else:
                print(err)
        cursor.close()
        self.CONEXION.close()
