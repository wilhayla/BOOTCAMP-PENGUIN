def lista_numeros (lista):
    lista02 = []
    for i in range(len(lista)):
        if lista[i] > 10:
            lista02.append(lista[i])
    return lista02
            

lista = [5,44,3,18,42,4]
lista_final = lista_numeros(lista)
print(f'La lista final es: {lista_final}')