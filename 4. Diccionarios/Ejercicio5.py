"""Escribir un programa que almacene el diccionario con los créditos 
de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
y después muestre por pantalla los créditos de cada asignatura en el formato 
<asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las 
asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar 
también el número total de créditos del curso.
"""
Curso={'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos=0
for i in Curso:
    print("{} tiene {} créditos".format(i,Curso[i]))
    total_creditos=total_creditos+Curso[i]
print("Total de créditos llevados:", total_creditos)