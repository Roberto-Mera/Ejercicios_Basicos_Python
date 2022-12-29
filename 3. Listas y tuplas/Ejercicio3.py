"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las 
muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde 
<asignatura> es cada una des las asignaturas de la lista y <nota> cada una de 
las correspondientes notas introducidas por el usuario.
"""
Cursos =["Matemática", "Física", "Química", "Historia", "Lengua"]
Notas=[]
for i in range(len(Cursos)):
    j=float(input("Ingrese nota del curso {}:".format(Cursos[i])))
    Notas=Notas+[j]
    i=i+1
for i in range(len(Cursos)):
    print("En {} has sacado {}".format(Cursos[i], Notas[i]))