"""
lista = list()
otra_lista = []
print(len(lista))
"""

listRange=[1,2,3,4,5,9,7,8,9,3,3,2,3,4,5]
# listRange = list(range(10))
print(listRange)

# print(listaStrings[0])
# print(listaStrings[-2])
print(listRange.count(3), 'se repite', listRange.count(3))

name, age, apellido = 'Luis', 33, 'Gonzalez'
print(name)
print(age)
print(apellido)

# print(listRange + listaStrings)
# print(listRange*2)

listaStrings = ['Hola Mundo','Como estas','Bienvenido']
listaStrings.append('final')
listaStrings.insert(-1,'intermedio')
print(listaStrings)


