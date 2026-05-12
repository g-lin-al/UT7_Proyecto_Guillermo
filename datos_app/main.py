from datos_app.cons import Cons


class App:

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

    def elegir_opcion(self) -> int:
        opc: int = -1
        opc = int(input("¿Opción? -> "))
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
        pass

    def crear_profesor(self):
        pass

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
        opc: int = -1
        print(self.imprimir_menu_principal())
        opc = self.elegir_opcion()
        while opc != Cons.OPC_8:
            if opc == Cons.OPC_1: # Crear usuario (Admin)
                print(opc)
                print(self.imprimir_menu_principal())
                self.elegir_opcion()
            elif opc == Cons.OPC_2: # Crear usuario (Profesor)
                print(opc)
                print(self.imprimir_menu_principal())
                self.elegir_opcion()
            elif opc == Cons.OPC_3: # Ver calendario de guardias
                print(opc)
                print(self.imprimir_menu_principal())
                self.elegir_opcion()
            elif opc == Cons.OPC_4: # Dar de alta guardias
                print(opc)
                print(self.imprimir_menu_principal())
                self.elegir_opcion()
            elif opc == Cons.OPC_5: # Dar de baja guardias
                print(opc)
                print(self.imprimir_menu_principal())
                self.elegir_opcion()
            elif opc == Cons.OPC_6: # Generar informe de guardias
                print(opc)
                print(self.imprimir_menu_principal())
                self.elegir_opcion()
            elif opc == Cons.OPC_7: # Generar listado de usuarios
                print(opc)
                print(self.imprimir_menu_principal())
                self.elegir_opcion()
            else:
                self.opcion_no_reconocida()


App().run()
print("Saliendo...")
