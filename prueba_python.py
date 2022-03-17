def conversor(valor, monedaPais):
    moneda = input("Introduce el valor de tu moneda " + monedaPais + " : ")
    moneda = float(moneda)
    valor_dolar = valor
    dolar = moneda / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("En dolares tienes $ " + dolar)


menu = """
Conversor de monedas 💰

1 - México
2 - Colombia
3 - Canada 
"""

print(menu)
opcion = input("Seleccione un opción: ")


if opcion == "1":
    conversor(19.85, "mexicana")
elif opcion == "2":
    conversor(3859, "colombiana")
elif opcion == "3":
    conversor(1.2, "canadience")
else:
    print("La opcion no es correcta. ")
