menu = ['hamburguesa', 'pizza', 'ensalada']
opcion01 = menu[0]
opcion02 = menu[1]
opcion03 = menu[2]

numero = int(input('Ingrese una opcion del menu del 1 al 3: '))
if numero == 1:
    print(f'Elegiste {opcion01}')
elif numero == 2:
    print(f'Elegiste {opcion02}')
else:
    print(f'Elegiste {opcion03}')
