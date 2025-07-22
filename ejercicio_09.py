age_person = int(input(f"Ingrese su edad: "))
day_week = input((f"Ingrese el dia de la semana: "))
is_student = input((f"¿Es estudiante? (Si o No): "))

if is_student.lower() == "si":
    price_tiket = 35
else:
    price_tiket = 50

if day_week.lower() not in ["miercoles","miércoles"]:
    if age_person >= 0 and age_person < 13:
        print(f"No puedes ver peliculas mayores de 15 años")
        print(f"Precio del ticket Q{price_tiket}")

    elif age_person >= 13 and age_person < 100:
        print(f"Precio del ticket Q{price_tiket}")

    else:
        print(f"Ingreso mal su edad")
else:
    if age_person >= 0 and age_person < 13:
        print(f"No puedes ver peliculas mayores de 15 años")
        print(f"Precio del ticket Q{price_tiket}")
        print(f"Oferta de miercoles 2x1")

    elif age_person >= 13 and age_person < 100:
        print(f"Precio del ticket Q{price_tiket}")
        print(f"Oferta de miercoles 2x1")

    else:
        print(f"Ingreso mal su edad")