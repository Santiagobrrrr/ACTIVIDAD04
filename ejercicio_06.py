weight_user = float(input("Ingrese el peso del paquete (kg): "))
distance_user = float(input("Ingrese la distancia en km: "))
urgency_user = input("¿Es urgente? (sí/no): ")
size_user = input("Tamaño del paquete (pequeño/mediano/grande): ")

if weight_user < 5 and urgency_user == "no":
    discount = -15
    is_true = "Por peso menor a 5 kg y no tener urgencia, tiene descuento de Q15"
else:
    discount = 0
    is_true = ""

if urgency_user == "si":
    surcharge_urgency = 50
    is_urgented = "Recargo por urgencia son Q50 más"
else:
    surcharge_urgency = 0
    is_urgented = "No tiene recargo urgencia (no se agrega costo)"

if size_user.lower == "grande":
    surcharge_size = 30
    is_size_big = "Recargo por tamaño grande son Q30 más"
else:
    surcharge_size = 0
    is_size_big = "No tiene recargo por tamaño"

if weight_user <= 5:
    price_per_distance = 0.5
    cost = 50
    base_cost = cost + (distance_user * price_per_distance)

elif weight_user >= 6 or weight_user<= 35:
    price_per_distance = 1
    cost = 100
    base_cost = cost + (distance_user * price_per_distance)

else:
    price_per_distance = 1.5
    cost = 150
    base_cost = cost + (distance_user * price_per_distance)

total_cost = base_cost + surcharge_size + surcharge_urgency + discount

print(f"El costo por paquete es: {cost}")
print(f"La distancia es de {distance_user}km como el peso del paquete era de {weight_user}kg el precio por km es de: Q{price_per_distance} ")
print(f"Total por distancia recorrida: Q{distance_user*price_per_distance}")
print(f"{is_urgented}")
print(f"{is_size_big}")
print(f"{is_true}")
print(f"El costo total es: {total_cost}")