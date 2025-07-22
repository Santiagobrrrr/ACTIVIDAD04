name_student1 = input(f"Ingrese el nombre del estudiante 1: ")
note_1_student = int(input(f"Ingrese la nota 1 de {name_student1}: "))
note_2_student = int(input(f"Ingrese la nota 2 de {name_student1}: "))
note_3_student = int(input(f"Ingrese la nota 3 de {name_student1}: "))

name_student2 = input(f"\nIngrese el nombre del estudiante 2: ")
note_1_student2 = int(input(f"Ingrese la nota 1 de {name_student2}: "))
note_2_student2 = int(input(f"Ingrese la nota 2 de {name_student2}: "))
note_3_student2 = int(input(f"Ingrese la nota 3 de {name_student2}: "))

name_student3 = input(f"\nIngrese el nombre del estudiante 3: ")
note_1_student3 = int(input(f"Ingrese la nota 1 de {name_student3}: "))
note_2_student3 = int(input(f"Ingrese la nota 2 de {name_student3}: "))
note_3_student3 = int(input(f"Ingrese la nota 3 de {name_student3}: "))

name_student4 = input(f"\nIngrese el nombre del estudiante 4: ")
note_1_student4 = int(input(f"Ingrese la nota 1 de {name_student4}: "))
note_2_student4 = int(input(f"Ingrese la nota 2 de {name_student4}: "))
note_3_student4 = int(input(f"Ingrese la nota 3 de {name_student4}: "))

name_student5 = input(f"\nIngrese el nombre del estudiante 5: ")
note_1_student5 = int(input(f"Ingrese la nota 1 de {name_student5}: "))
note_2_student5 = int(input(f"Ingrese la nota 2 de {name_student5}: "))
note_3_student5 = int(input(f"Ingrese la nota 3 de {name_student5}: "))

prom1 = (note_1_student + note_2_student + note_3_student) / 3
prom2 = (note_1_student2 + note_2_student2 + note_3_student2) / 3
prom3 = (note_1_student3 + note_2_student3 + note_3_student3) / 3
prom4 = (note_1_student4 + note_2_student4 + note_3_student4) / 3
prom5 = (note_1_student5 + note_2_student5 + note_3_student5) / 3

if prom1 < 70 and prom2 < 70 and prom3 < 70 and prom4 < 70 and prom5 < 70:
    if note_1_student + 5 > 100:
        note_1_student = 100
    else:
        note_1_student = note_1_student + 5
    if note_2_student + 5 > 100:
        note_2_student = 100
    else:
        note_2_student = note_2_student + 5
    if note_3_student + 5 > 100:
        note_3_student = 100
    else:
        note_3_student = note_3_student + 5
    if note_1_student2 + 5 > 100:
        note_1_student2 = 100
    else:
        note_1_student2 = note_1_student2 + 5
    if note_2_student2 + 5 > 100:
        note_2_student2 = 100
    else:
        note_2_student2 = note_2_student2 + 5
    if note_3_student2 + 5 > 100:
        note_3_student2 = 100
    else:
        note_3_student2 = note_3_student2 + 5
    if note_1_student3 + 5 > 100:
        note_1_student3 = 100
    else:
        note_1_student3 = note_1_student3 + 5
    if note_2_student3 + 5 > 100:
        note_2_student3 = 100
    else:
        note_2_student3 = note_2_student3 + 5
    if note_3_student3 + 5 > 100:
        note_3_student3 = 100
    else:
        note_3_student3 = note_3_student3 + 5
    if note_1_student4 + 5 > 100:
        note_1_student4 = 100
    else:
        note_1_student4 = note_1_student4 + 5
    if note_2_student4 + 5 > 100:
        note_2_student4 = 100
    else:
        note_2_student4 = note_2_student4 + 5
    if note_3_student4 + 5 > 100:
        note_3_student4 = 100
    else:
        note_3_student4 = note_3_student4 + 5
    if note_1_student5 + 5 > 100:
        note_1_student5 = 100
    else:
        note_1_student5 = note_1_student5 + 5
    if note_2_student5 + 5 > 100:
        note_2_student5 = 100
    else:
        note_2_student5 = note_2_student5 + 5
    if note_3_student5 + 5 > 100:
        note_3_student5 = 100

prom1 = (note_1_student + note_2_student + note_3_student) / 3
prom2 = (note_1_student2 + note_2_student2 + note_3_student2) / 3
prom3 = (note_1_student3 + note_2_student3 + note_3_student3) / 3
prom4 = (note_1_student4 + note_2_student4 + note_3_student4) / 3
prom5 = (note_1_student5 + note_2_student5 + note_3_student5) / 3

print(f"\nTabla")
print(f"Nombre y Promedio")
print(f"{name_student1} - {prom1}")
print(f"{name_student2} - {prom2}")
print(f"{name_student3} - {prom3}")
print(f"{name_student4} - {prom4}")
print(f"{name_student5} - {prom5}")