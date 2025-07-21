prices_list = []
count_value = int(input("Ingrese el valor de productos a pagar: "))
for i in range(0,count_value):
    value_product = float(input("Ingrese el valor del producto: Q"))
    prices_list.append(value_product)
user_tip = input(f"Desea agregar propina: ").lower()
if user_tip == "si":
    percentage = float(input("¿Cuanto %? "))
    percentage2 = percentage / 100
else:
    percentage2 = 0
frequent_card = input(f"Tiene tarjeta de cliente preferencial? (si o no): ").lower()
if frequent_card == "si":
    discount_card = 0.1
else:
    discount_card = 0


print(f"Subtotal: Q{sum(prices_list)}")
print(f"Subtotal con descuento: Q{(sum(prices_list))-(sum(prices_list)*discount_card)}")
print(f"Propina: {(sum(prices_list) * percentage2)}")
print(f"Total (con IVA incluido): {(((sum(prices_list))-(sum(prices_list)*discount_card))*1.12)+(sum(prices_list) * percentage2)}")