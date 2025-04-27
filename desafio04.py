def eliminar_elemento(numeros, posicion):
    print('Funcion que elimina un elemento de la lista.')
    print('--------------------------------------------')
    print(numeros)
    print('--------------------------------------------')
    if posicion == 1:
        numeros.pop(0)
    elif posicion == 2:
        numeros.pop(1)
    elif posicion == 3:
         numeros.pop(2)
    elif posicion == 4:
        numeros.pop(3)
    elif posicion == 5:
        numeros.pop(4)
    elif posicion == 6:
        numeros.pop(5)
    elif posicion == 7:
        numeros.pop(6)
            
    print(f'La posicion de la lista a eliminar es {posicion}.')
    print(f'La lista final es: {numeros}')

lista = [1,2,3,4,5,6,7]
posicion = int(input('Que posicion de la lista quieres eliminar?: '))
eliminar_elemento(lista, posicion)
        