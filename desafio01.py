def evaluar_estudiante(nombre, nota1, nota2, nota3):
    print(f'Hola {nombre}. Voy a calcular el promedio de tus notas.')
    print('------------------------------------------------------------')
    suma_notas = nota1 + nota2 + nota3
    promedio = suma_notas / 3
    return promedio

nombre = 'Jorge'
promedio_estudiante = evaluar_estudiante(nombre, 5, 3, 3)
if promedio_estudiante >= 6:
    print(f'Felicitaciones {nombre}, aprobaste con un promedio de {promedio_estudiante}!')
else:
    print(f'Lo siento {nombre}, reprobaste con un promedio de {promedio_estudiante}!')
    