day_user1 = int(input(f"Ingrese el número de dia de la fecha 1: "))
month_user1 = int(input(f"Ingrese el número de mes de la fecha 1: "))
year_user1 = int(input(f"Ingrese el número de año de la fecha 1: "))

day_user2 = int(input(f"Ingrese el número de dia de la fecha 2: "))
month_user2 = int(input(f"Ingrese el número de mes de la fecha 2: "))
year_user2 = int(input(f"Ingrese el número de año de la fecha 2: "))

if year_user1 == year_user2:
    if month_user1 == month_user2:
        if day_user1 > day_user2:
            print(f"La fecha 1 es mayor que la fecha 2")
        elif day_user2 > day_user1:
            print(f"La fecha 1 es mayor que la fecha 2")
        elif day_user1 == day_user2:
            print(f"Ni una fecha es mayor que otra")
        else:
            print(f"Ha ingresado un valor incorrecto")
    elif month_user1 > month_user2:
        print(f"La fecha 1 es mayor que la fecha 2")
    elif month_user2 > month_user1:
        print(f"La fecha 2 es mayor que la fecha 1")
    else:
        print(f"Ha ingresado un valor incorrecto")
elif year_user1 > year_user2:
    print(f"La fecha 1 es mayor que la fecha 2")
elif year_user2 > year_user1:
    print(f"La fecha 2 es mayor que la fecha 1")
else:
    print(f"Ha ingresado un valor incorrecto")

if month_user1 == month_user2 and year_user1 == year_user2:
    print(f"Las dos fechas se encuentran en el mismo mes y año")
elif year_user1 != year_user2 or month_user1 != month_user2:
    print(f"No se encuentran en el mismo mes o año")

if day_user1 > 0 and day_user2 > 0:
    if day_user1 > day_user2:
        print(f"La diferencia entre dias es de: {day_user1} - {day_user2}")
    elif day_user2 > day_user1:
        print(f"La diferencia entre dias es de: {day_user2} - {day_user1}")
    elif day_user1 == day_user2:
        print(f"No hay diferencia de dias")
    else:
        print(f"Ha ingresado un valor incorrecto")