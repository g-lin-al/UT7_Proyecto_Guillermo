import datetime
import mysql
from mysql.connector import errorcode
from datos_app.bbdd import BaseDatos
from datos_app.cons import Cons
from datos_centro.guardias import Guardia
from datos_personal.profesores import Profesor
from ficheros.config import Config


class App:
    CONEXION = Config.cnx

    def imprimir_menu_principal(self):
        return (f"{Cons.SEPARADOR * 25}\n"
                f"{Cons.OPC_1} - Crear usuario (Admin)\n"
                f"{Cons.OPC_2} - Crear usuario (Profesor)\n"
                f"{Cons.OPC_3} - Ver calendario de guardias\n"
                f"{Cons.OPC_4} - Dar de alta guardias\n"
                f"{Cons.OPC_5} - Dar de baja guardias\n"
                f"{Cons.OPC_6} - Generar informe de guardias\n"
                f"{Cons.OPC_7} - Generar listado de usuarios\n"
                f"{Cons.OPC_8} - Salir de la aplicación\n")

    def elegir_opcion(self) -> str:
        opc: str = "-1"
        opc = input("¿Opción? -> ")
        return opc

    def realizar_nueva_operacion(self):
        opc: str = "-1"
        print(f"¿Realizar otra operación?\n"
              f"{Cons.OPC_1} - Sí\n"
              f"{Cons.OPC_2} - No\n")
        opc = self.elegir_opcion()
        if opc == Cons.OPC_1:
            return Cons.OPC_1
        elif opc == Cons.OPC_2:
            return Cons.OPC_2
        else:
            self.opcion_no_reconocida()

    def opcion_no_reconocida(self):
        print(f"Opción no reconocida. ¿Intentar de nuevo?\n"
              f"{Cons.OPC_1} - Sí\n"
              f"{Cons.OPC_2} - No\n")
        opc = self.elegir_opcion()
        if opc == Cons.OPC_1:
            return Cons.OPC_1
        elif opc == Cons.OPC_2:
            return Cons.OPC_2
        else:
            self.opcion_no_reconocida()

    def crear_admin(self, id: str, nombre: str, clave: str) -> Profesor:
        adm: Profesor = Profesor(id, nombre, "ADMIN", clave)
        return adm

    def crear_profesor(self, id: str, nombre: str, apellidos: str, clave: str) -> Profesor:
        prof: Profesor = Profesor(id, nombre, apellidos, clave)
        return prof

    def insertar_profesor(self, prof: Profesor):
        cursor = self.CONEXION.cursor()
        self.CONEXION.autocommit = True
        aniadir_prof = ("INSERT INTO profesores (id, nombre, apellidos, clave)" +
                        f" VALUES ('{prof.id}', '{prof.nombre}', '{prof.apellido}', '{prof.clave}')")
        try:
            cursor.execute(aniadir_prof)
            print(f"Añadido profesor {prof.nombre} (id: {prof.id}).")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de conexión.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe dicha base de datos.")
            else:
                print(err)
        cursor.close()

    def ver_calendario(self):
        pass

    def dar_alta_guardia(self, id: str, dia: datetime.date, hora: str, curso: str, clase: str, tarea: str, fichero: str):
        guardia: Guardia = Guardia(id, dia, hora, curso, clase, tarea)
        cursor = self.CONEXION.cursor()
        self.CONEXION.autocommit = True
        aniadir_guardia = ("INSERT INTO guardias (id, dia, hora, curso, aula, tarea, ficheros)" +
                        f" VALUES ('{guardia.id}', '{guardia.dia}', '{guardia.hora}', '{guardia.curso}',"
                        f" '{guardia.clase}', '{guardia.tarea}', '{guardia.ficheros}')")
        try:
            cursor.execute(aniadir_guardia)
            print(f"Añadida la guardia el día {guardia.dia} en la clase {guardia.clase}.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de conexión.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe dicha base de datos.")
            else:
                print(err)
        cursor.close()

    def dar_baja_guardia(self, id: str, dia: datetime.date, hora: str):
        cursor = self.CONEXION.cursor()
        self.CONEXION.autocommit = True
        borrar_guardia = (f"DELETE FROM guardias "
                          f"WHERE id = '{id}' "
                          f"AND dia = {dia} "
                          f"AND hora = '{hora}'")
        try:
            cursor.execute(borrar_guardia)
            print(f"Eliminada la guardia del día {dia} a las {hora} horas.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de conexión.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe dicha base de datos.")
            else:
                print(err)
        cursor.close()

    def generar_inf_guardias(self, f_ini: datetime.date, f_fin: datetime.date):
        cursor = self.CONEXION.cursor()
        self.CONEXION.autocommit = True
        busqueda = (f"select * from guardias where"
                    f"{dia} between '{f_ini}' and '{f_fin}'")
        try:
            cursor.execute(busqueda)
            for id, dia, hora, curso, aula, tarea, ficheros in cursor:
                print(f"Guardia ID {id}:\n"
                      f"Día {dia} a las {hora} horas\n"
                      f"Curso: {curso}, aula {aula}\n"
                      f"Tarea -> {tarea}")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de conexión.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe dicha base de datos.")
            else:
                print(err)
        cursor.close()

    def generar_listado_usuarios(self, tipo: str):
        cursor = self.CONEXION.cursor()
        self.CONEXION.autocommit = True
        listar_usuarios: str = f"SELECT id, nombre, apellidos FROM profesores"
        if tipo == Cons.OPC_1:
            listar_usuarios = listar_usuarios + " where apellidos != 'ADMIN'"
            try:
                cursor.execute(listar_usuarios)
                for id, nombre, apellido in cursor:
                    print(f"ID: {id} - {nombre} {apellido}")
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Error de conexión.")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("No existe dicha base de datos.")
                else:
                    print(err)
        elif tipo == Cons.OPC_2:
            listar_usuarios = listar_usuarios + " where apellidos = 'ADMIN'"
            try:
                cursor.execute(listar_usuarios)
                for id, nombre, apellido in cursor:
                    print(f"ID: {id} - {nombre}")
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Error de conexión.")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("No existe dicha base de datos.")
                else:
                    print(err)
        else:
            print("Opción no válida.")
        cursor.close()

    def cargar_inicio(self):
        fichero: str = "carga_inicial.txt"
        sentencias: list[str] = []
        cursor = self.CONEXION.cursor()
        self.CONEXION.autocommit = True
        with open(fichero, 'r', encoding='utf-8') as fich:
            sentencias = fich.readlines()
            for num, sent in enumerate(sentencias):
                try:
                    cursor.execute(sent.strip("\n"))
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Error de conexión.")
                    elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("No existe dicha base de datos.")
                    else:
                        print(err)

    def run(self):
        self.cargar_inicio()
        BaseDatos().cargar_profesores()
        BaseDatos().cargar_admins()
        opc: str = "-1"
        while opc != Cons.OPC_8:
            print(self.imprimir_menu_principal())
            opc = self.elegir_opcion()
            if opc == Cons.OPC_1:  # Crear usuario (Admin)
                id: str = input("ID del Admin.: ")
                nombre: str = input("Nombre del Admin.: ")
                clave: str = input("Clave del profesor: ")
                self.insertar_profesor(self.crear_admin(id, nombre, clave))
                continue
            elif opc == Cons.OPC_2: # Crear usuario (Profesor)
                id: str = input("ID del profesor: ")
                nombre: str = input("Nombre del profesor: ")
                apellidos: str = input("Apellidos del profesor: ")
                clave: str = input("Clave del profesor: ")
                self.insertar_profesor(self.crear_profesor(id, nombre, apellidos, clave))
                continue
            elif opc == Cons.OPC_3: # Ver calendario de guardias
                fecha_ini: datetime.date
            elif opc == Cons.OPC_4: # Dar de alta guardias
                id: str = input("ID del profesor de guardia: ")
                dia: int = int(input("Día de la guardia: "))
                mes: int = int(input("Mes (1-12): "))
                anio: int = int(input("Año: "))
                hora: str = input("Hora de la guardia (1-6): ")
                curso: str = input("Curso de guardia (primero, segundo): ")
                clase: str = input("Clase en la que se realiza la guardia (1-6 ó biblioteca): ")
                tarea: str = input("¿Tarea asignada a la guardia? (S/N): ")
                fecha = datetime.datetime(anio, mes, dia)
                if tarea == "S":
                    fichero: str = input("Texto de la tarea: ")
                else:
                    fichero = ""
                self.dar_alta_guardia(id, fecha, hora, curso, clase, tarea, fichero)
            elif opc == Cons.OPC_5: # Dar de baja guardias
                id: str = input("ID del profesor de guardia: ")
                dia: str = input("Día de la guardia: ")
                hora: str = input("Hora de la guardia: ")
                self.dar_baja_guardia(id, dia, hora)
            elif opc == Cons.OPC_6: # Generar informe de guardias
                dia_ini: int = int(input("Día de inicio de la búsqueda: "))
                mes_ini: int = int(input("Mes (1-12): "))
                anio_ini: int = int(input("Año: "))
                dia_fin: int = int(input("Día de inicio de la búsqueda: "))
                mes_fin: int = int(input("Mes (1-12): "))
                anio_fin: int = int(input("Año: "))
                fecha_ini: date = datetime.date(dia_ini, mes_ini, anio_ini)
                fecha_fin: date = datetime.date(dia_fin, mes_fin, anio_fin)
                generar_inf_guardias(fecha_ini, fecha_fin)
            elif opc == Cons.OPC_7: # Generar listado de usuarios
                opc = input("1.- Listado de Profesores\n"
                            "2.- Listado de Admins.\n"
                            "-> ")
                self.generar_listado_usuarios(opc)
            elif opc == Cons.OPC_8:
                print("Saliendo...")
                self.CONEXION.close()
            else:
                print("Opción no reconocida")


App().run()
