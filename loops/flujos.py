# if <expresion>:  # base
#     <bloque>
# elif <expresion>:  # 0..n
#     <bloque>
# else:             # 0 o 1
#     <bloque>


# a = 6
# if a > 2:
#     print("a < 2")
# elif foo == 6:
#     print("wtf")


# for nombre in iterable:
#    <bloque>


# lista = [(1, 2), (4, 5)]
# for a, b in lista:
#     print(a, b)

# while <expresion>:
#     <bloque>

# try:
#     bloque
# except:     0 .. n, específicos o generales
#     bloque
# else:       0 o 1
#     bloque
# finally:    0 o 1
#     bloque


# a = 7
# while a > 0:
#     print(a)
#     a -= 1
#     if a == 4:
#         break
# else:
#     print("todo bien")

# lista = [1, 2, 3, 4, 5, 6]
# for i in lista:
#     print(i)
#     if i == 4:
#         break
# else:
#     print("todo bien")

# nros = [3, 5, 7, -3, 0, 2, 3, 7, 3]
# cuad = [nro ** 2 for nro in nros]
# print("cuad", cuad)
# cuad = [nro ** 2 for nro in nros if nro != 0]
# print("cuad sincero", cuad)

nros = [3, 5, 7, -3, 0, 2, 3, 7, 3]
cuad = [nro ** 2 for nro in nros]
print("list comprehension", cuad)
cuad = {nro ** 2 for nro in nros}  # set([nro ** 2 for nro in nros])
print("set comprehension", cuad)
cuad = {nro: nro ** 2 for nro in nros}
print("dict comprehension", cuad)
cuad = (nro ** 2 for nro in nros)
print("generator comprehension", cuad)
print("suma", sum(nro ** 2 for nro in nros))
print("suma", sum([nro ** 2 for nro in nros]))
