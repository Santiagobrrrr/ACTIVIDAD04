coord_1 = input("Ingrese la coordenada 1  (ej. norte, sur, este, oeste): ")
coord_2 = input("Ingrese la coordenada 2  (ej. norte, sur, este, oeste): ")

if coord_1.lower() == "norte":
    if coord_2.lower() == "sur":
        print("Recto hacia el sur")
    elif coord_2.lower() == "este":
        print("La direccion es noreste")
    elif coord_2.lower() == "oeste":
        print("La direccion es noroeste")

if coord_1.lower() == "sur":
    if coord_2.lower() == "norte":
        print("Recto hacia el norte")
    elif coord_2.lower() == "este":
        print("La direccion es sureste")
    elif coord_2.lower() == "oeste":
        print("La direccion es suroeste")

if coord_1.lower() == "este":
    if coord_2.lower() == "oeste":
        print("Recto hacia el oeste")
    elif coord_2.lower() == "norte":
        print("La direccion es noreste")
    elif coord_2.lower() == "sur":
        print("La direccion es sureste")

if coord_1.lower() == "oeste":
    if coord_2.lower() == "este":
        print("Recto hacia el este")
    elif coord_2.lower() == "norte":
        print("La direccion es noreste")
    elif coord_2.lower() == "sur":
        print("La direccion es suroeste")