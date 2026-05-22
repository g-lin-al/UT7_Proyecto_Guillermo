import mysql
from mysql.connector import errorcode
from ficheros.config import Config


class BaseDatos:
    CONEXION = Config.cnx
    PROF = Config.PROF_TXT
    ADM = Config.ADM_TXT

    def cargar_profesores(self):
        cursor = self.CONEXION.cursor()
        self.CONEXION.autocommit = True
        recoger_prof = "SELECT * FROM profesores where apellidos != 'ADMIN'"
        try:
            cursor.execute(recoger_prof)
            with open(self.PROF, 'w', encoding='utf-8') as f:
                for id, nombre, apellidos, clave in cursor:
                    f.write(id + "," + nombre + "," + apellidos + "," + clave + "\n")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de conexión.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe dicha base de datos.")
            else:
                print(err)
        cursor.close()

    def cargar_admins(self):
        cursor = self.CONEXION.cursor()
        self.CONEXION.autocommit = True
        recoger_adm = "SELECT * FROM profesores where apellidos = 'ADMIN'"
        try:
            cursor.execute(recoger_adm)
            with open(self.ADM, 'w', encoding='utf-8') as f:
                for id, nombre, apellidos, clave in cursor:
                    f.write(id + "," + nombre + "," + apellidos + "," + clave + "\n")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de conexión.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe dicha base de datos.")
            else:
                print(err)
        cursor.close()
