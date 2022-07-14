pesos = float (input("¿cuántos pesos méxicanos tienes?: "))
valor_dolar = 20.84
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
