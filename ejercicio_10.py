day_user1 = int(input("Ingrese el número de día de la fecha 1: "))
month_user1 = int(input("Ingrese el número de mes de la fecha 1: "))
year_user1 = int(input("Ingrese el número de año de la fecha 1: "))

day_user2 = int(input("Ingrese el número de día de la fecha 2: "))
month_user2 = int(input("Ingrese el número de mes de la fecha 2: "))
year_user2 = int(input("Ingrese el número de año de la fecha 2: "))

if month_user1 == month_user2 and year_user1 == year_user2:
    print("Las dos fechas se encuentran en el mismo mes y año")
else:
    print("No se encuentran en el mismo mes o año")

if year_user1 > year_user2:
    print("La fecha 1 es mayor que la fecha 2")
elif year_user2 > year_user1:
    print("La fecha 2 es mayor que la fecha 1")
else:
    if month_user1 > month_user2:
        print("La fecha 1 es mayor que la fecha 2")
    elif month_user2 > month_user1:
        print("La fecha 2 es mayor que la fecha 1")
    else:
        if day_user1 > day_user2:
            print("La fecha 1 es mayor que la fecha 2")
        elif day_user2 > day_user1:
            print("La fecha 2 es mayor que la fecha 1")
        elif day_user1 == day_user2:
            print("Ni una fecha es mayor que otra")
        else:
            print("Ha ingresado un valor incorrecto")

if day_user1 > 0 and day_user2 > 0:
    if day_user1 == day_user2:
        print("No hay diferencia de días")
    elif day_user1 > day_user2:
        print(f"La diferencia entre días es de: {day_user1 - day_user2}")
    else:
        print(f"La diferencia entre días es de: {day_user2 - day_user1}")
else:
    print("Ha ingresado un valor incorrecto")
