import mysql
from mysql.connector import errorcode
from datos_app.cons import Cons
from datos_personal.profesores import Profesor


class App:
    CONEXION = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='proyecto')

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
        opc: int = -1
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

    def carga_datos(self):
        pass

    def crear_admin(self):
        pass # IDEA -> meter los admins como profesores con el apellido "ADMIN" y así poder filtrarlos

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
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:  # errno dependerá de la libería
                print("Error de conexión.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe dicha base de datos.")
            else:
                print(err)
        cursor.close()
        self.CONEXION.close()

    def ver_calendario(self):
        pass

    def dar_alta_guardia(self):
        pass

    def dar_baja_guardia(self):
        pass

    def generar_inf_guardias(self):
        pass

    def generar_listado_usuarios(self):
        pass

    def run(self):
        opc: str = "-1"
        while opc != Cons.OPC_8:
            print(self.imprimir_menu_principal())
            opc = self.elegir_opcion()
            if opc == Cons.OPC_1:  # Crear usuario (Admin)
                print(opc)
            elif opc == Cons.OPC_2: # Crear usuario (Profesor)
                id: str = input("ID del profesor: ")
                nombre: str = input("Nombre del profesor: ")
                apellidos: str = input("Apellidos del profesor: ")
                clave: str = input("Clave del profesor: ")
                self.insertar_profesor(self.crear_profesor(id, nombre, apellidos, clave))
                continue
            elif opc == Cons.OPC_3: # Ver calendario de guardias
                print(opc)
            elif opc == Cons.OPC_4: # Dar de alta guardias
                print(opc)
            elif opc == Cons.OPC_5: # Dar de baja guardias
                print(opc)
            elif opc == Cons.OPC_6: # Generar informe de guardias
                print(opc)
            elif opc == Cons.OPC_7: # Generar listado de usuarios
                print(opc)
            elif opc == Cons.OPC_8:
                print("Saliendo...")
            else:
                print("Opción no reconocida")


App().run()
