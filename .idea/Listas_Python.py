mi_lista = [1 , 2, 3, 4, 5]
print("lista inicial:", mi_lista)

mi_lista.append (6)
print("despues de append(6):", mi_lista)

mi_lista.insert (6,7)
print("despues de insert(5,7):", mi_lista)

mi_lista.remove(7)
print("despues de remove(7):",mi_lista)

del mi_lista [1]
print("despues de eliminar el 1 de mi lista inicial (2):",mi_lista)

ultimo = mi_lista.pop()
print("elemento eliminado con .pop():", ultimo)
print("despues de pop():", mi_lista)

print("Primer elemento:", mi_lista[0])
print("último elemento:", mi_lista[-1])

print("Recorriendo la lista:")
for numero in mi_lista:
    print(numero)
mi_lista.sort()
print("lista ordenada:", mi_lista)
mi_lista.reverse()
print("lista orden inverso:", mi_lista)



