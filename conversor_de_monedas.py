def conversor(moneda, valor_dolar):
    pesos = float(input('¿Cuantos ' + 'pesos ' + moneda + ' tienes?'))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares =str(dolares)
    print('tienes$ ' +  dolares + ' dolares' )

Menu = """ 
Bienvenido al conversor de monedas, elige una opción

1 - Pesos Mexicanos
2 - Pesos Argentinos
3 - Pesos Colombianos

 Elige una opción """

opcion = int(input(Menu))

if opcion == 1:
    conversor("Mexicanos", 20.40)

elif opcion == 2:
    conversor("Argentinos", 129.16)

elif opcion == 3:
    conversor("colombianos", 4317)

else:
    print('por favor, escoge una opción correcta')
