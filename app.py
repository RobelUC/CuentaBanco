from cuenta_banco import CuentaBanco


def mostrar_menu():
    """Imprime las opciones del menú en consola."""
    print("\n" + "=" * 30)
    print("       BANCO PICHINCHA     ")
    print("=" * 30)
    print("1. Depósito")
    print("2. Retiro")
    print("3. Transferencia")
    print("4. Consultar Saldo")
    print("5. Salir")
    print("=" * 30)


def main():
    """Función principal que ejecuta el bucle de la aplicación."""
    print("Inicializando sistema...")
    
    # Instancias de prueba
    mi_cuenta = CuentaBanco("Usuario Principal", 1000.0)
    cuenta_secundaria = CuentaBanco("Cuenta Amigo", 500.0)

    while True:
        mostrar_menu()
        opcion = input(" Seleccione una opción: ")

        if opcion == '5':
            print("\n ¡Gracias por usar Banco Python!")
            break

        try:
            if opcion == '1':
                entrada = input("Ingrese monto a depositar: ")
                monto = float(entrada)
                mi_cuenta.deposito_cuenta(monto)

            elif opcion == '2':
                entrada = input("Ingrese monto a retirar: ")
                monto = float(entrada)
                mi_cuenta.retiro_cuenta(monto)

            elif opcion == '3':
                print(f"--- Destino: {cuenta_secundaria.titular} ---")
                entrada = input("Ingrese monto a transferir: ")
                monto = float(entrada)
                mi_cuenta.transferencia_cuenta(monto, cuenta_secundaria)

            elif opcion == '4':
                saldo = mi_cuenta.saldo_cuenta()
                print(f" Su saldo actual es: ${saldo:.2f}")

            else:
                print(" Opción no válida, intente nuevamente.")

        except ValueError as error_valor:
            # Captura errores de números negativos, saldo insuficiente o texto
            print(f" Error de valor: {error_valor}")
        
        except TypeError as error_tipo:
            # Captura errores de tipos de datos incorrectos
            print(f" Error de tipo: {error_tipo}")
            
        except Exception as error_inesperado:
            # Captura cualquier otro error para que el programa no colapse
            print(f" Error inesperado: {error_inesperado}")

if __name__ == "__main__":
    main()