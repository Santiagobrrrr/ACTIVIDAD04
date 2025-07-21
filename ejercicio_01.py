full_name_person = input(f"Ingrese su nombre completo: ")
dpi_person = input(f"Ingrese su dpi sin guiones ni espacios: ")
department_person = input(f"Ingrese su departamento: ")
year_birth_person = int(input(f"Ingrese su ano de nacimiento: "))

if department_person != ("petén" or "Petén" or "Alta Verapaz" or "alta verapaz"):
    if year_birth_person <= 2007:
        if len(full_name_person) > 5:
            if len(dpi_person) == 13:
                print(f"Bienvenido {full_name_person}, su centro de votación esta en: {department_person}")
            else:
                print(f"Su DPI es inválido")
        else:
            print(f"Su nombre no puede ser menor a 5 letras")
    else:
        print(f"No es mayor de edad")

if department_person == ("petén" or "Petén" or "Alta Verapaz" or "alta verapaz"):
    if year_birth_person <= 2008:
        if len(full_name_person) > 5:
            if len(dpi_person) == 13:
                print(f"Bienvenido {full_name_person}, su centro de votación esta en: {department_person}")
            else:
                print(f"Su dpi es inválido")
        else:
            print(f"Su nombre no puede ser menor a 5 letras")
    else:
        print(f"No es mayor de edad")

