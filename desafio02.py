def nombre_mas_largo(nombres):
    nombre01 = nombres[0]
    nombre02 = nombres[1]
    nombre03 = nombres[2]
    print(nombre01, nombre02, nombre03)
    if len(nombre01) > len(nombre02) and len(nombre01) > len(nombre03):
        return nombre01
    elif len(nombre02) > len(nombre03):
        return nombre02
    else:
        return nombre03

# MAIN
lista_nombres = ['william', 'pablo', 'estanislao']
nombre = nombre_mas_largo(lista_nombres)
print(f'El nombre mas largo es {nombre}')



