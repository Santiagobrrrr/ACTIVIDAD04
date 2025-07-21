department_person = input("Ingrese un departamento: ")
if department_person.lower() not in ["petén","alta verapaz"]:
    year_birth_person = int(input("Ingrese su año de nacimiento: "))
    if year_birth_person <= 2007:
        dpi_person = input("Ingrese su dpi sin guiones ni espacio: ")
        if len(dpi_person) == 13:
            full_name_person = input("Ingrese su nombre: ")
            if len(full_name_person) > 5:
                print(f"Bienvenido {full_name_person}, su centro de votación esta en: {department_person}")
            else:
                print(f"Su nombre tiene que ser mayor de 5 letras")
        else:
            print(f"DPI invalido")
    else:
        print(f"Es menor de edad, no puede votar")
else:
    year_birth_person = int(input("Ingrese su año de nacimiento: "))
    if year_birth_person >= 2008:
        dpi_person = input("Ingrese su dpi sin guiones ni espacio: ")
        if len(dpi_person) == 13:
            full_name_person = input("Ingrese su nombre: ")
            if len(full_name_person) > 5:
                print(f"Bienvenido {full_name_person}, su centro de votación esta en: {department_person}")
            else:
                print(f"Su nombre tiene que ser mayor de 5 letras")
        else:
            print(f"DPI invalido")
    else:
        print(f"Es menor de edad, no puede votar")