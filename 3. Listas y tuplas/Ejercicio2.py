"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje 
Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""
Cursos =["Matemática", "Física", "Química", "Historia", "Lengua"]
for i in range(len(Cursos)):
    print("Yo estudio {}".format(Cursos[i]))
    i=i+1