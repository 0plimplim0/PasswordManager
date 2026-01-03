import time
import functions

while True:
    functions.clear_console()
    print("========================================\n      ADMINISTRADOR DE CONTRASEÑAS      \n========================================")
    print("Bienvenido al administrador de contraseñas v1.0.0!\n\nPara empezar, selecciona una opción: \n")
    print("1. Generar contraseña.\n2. Agregar contraseña.\n3. Ver contraseñas.\n4. Salir.\n")
    user_selection = input("Seleccion: ")
    if (user_selection == "1"):
        try:
            functions.clear_console()
            print("=== GENERAR CONTRASEÑA ===")
            num_char = int(input("Longitud de la contraseña: "))
            num_symbols = int(input("Cantidad de simbolos: "))
            num_numbers = int(input("Cantidad de números: "))

            password = functions.generate_password(num_char, num_symbols, num_numbers)
            print(f"\nTu contraseña es: {password}\n")
            while True:
                user_selection = input("Deseas guardarla?(Y / N) ").lower()
                if (user_selection == "y"):
                    functions.menu_guardar(password)
                    time.sleep(1)
                    break
                elif (user_selection == "n"):
                    break
        except:
            print("Ha ocurrido un error.")
    elif (user_selection == "2"):
        functions.menu_guardar()
        time.sleep(1)
    elif (user_selection == "3"):
        functions.menu_ver()
    elif (user_selection == "4"):
        print("Saliendo...")
        time.sleep(0.5)
        break
    else:
        print("Por favor selecciona una opción válida.")
        time.sleep(1)