annual_income = int(input("Ingrese su ingreso anual: Q"))
dependents = int(input("Ingrese la cantidad de dependientes: "))

if annual_income < 40000 and dependents > 2:
    print(f"No paga impuestos")
elif annual_income >= 0 and annual_income <= 30000:
    total = annual_income * 0.05 + dependents * 1000
    print(f"Tiene de impuestos a pagar: Q{total}")
elif annual_income >= 30001 and annual_income <= 60000:
    total = annual_income * 0.1 + dependents * 1000
    print(f"Tiene de impuestos a pagar: Q{total}")
elif annual_income >= 60001 and annual_income <= 100000:
    total = annual_income * 0.15 + dependents * 1000
    print(f"Tiene de impuestos a pagar: Q{total}")
elif annual_income > 100000:
    total = annual_income * 0.2 + dependents * 1000
    print(f"Tiene de impuestos a pagar: Q{total}")