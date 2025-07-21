user_list = {"user1":"123", "user2":"12345", "user3":"123456"}

user_input = input(f"Ingrese su usuario: ")
if user_input in user_list:
    password_input = input(f"Ingrese su contraseña: ")
    if password_input == user_list[user_input]:
        print(f"Bienvenido {user_input}\n1- Ver perfil\n2- Cambiar contraseña\n3- Cerrar sesión")
    else:
        print(f"Repita nuevamente")
        password_input = input(f"Ingrese su contraseña: ")
        if password_input == user_list[user_input]:
            print(f"Bienvenido {user_input}\n1- Ver perfil\n2- Cambiar contraseña\n3- Cerrar sesión")
        else:
            print(f"Repita nuevamente")
            password_input = input(f"Ingrese su contraseña: ")
            if password_input == user_list[user_input]:
                print(f"Bienvenido {user_input}\n1- Ver perfil\n2- Cambiar contraseña\n3- Cerrar sesión")
            else:
                print(f"ACCESO BLOQUEADO")
else:
    print(f"Usuario incorrecto")