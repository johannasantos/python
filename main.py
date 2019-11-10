
# strings
nombre = 'jo '
apellido = "santos"
print(nombre + apellido)

# concatenacion de strings 

variable = 'hola ' + 'como estas'
print(variable)
variable2 = variable + ' mi nombre es jo'
print(variable2)


saludo = "HOLAAAA"

# dir es una funcion para ver los metodos y propiedades de un objeto  
print(dir(saludo))

# swapcase es un metodo para hacer que el string se vea en lower case 
print(saludo.lower())

# convenciones mas usadas para nombrar una variable 

camelCase = ""
snake_case = ""

# numeros

# enteros (int)

print(14 + 1)

numer5656565AAA6 = 1
print(numer5656565AAA6)

# decimales (float)

numero_float = 1.4
print(numero_float)

# booleanos

x = True
y = False

print('x and y is', x and y)

print('x or y is', x or y)

print('not x is', not x)

# listas

comidas = ["queso", "fideos", 'cebolla', 11, True, False, "condimentos",["legumbres", ""]]
print(comidas)

# len se usa para saber el largo de una lista 

print(len(comidas))
#usamos [] para saber la posicion de un elemento 

print(comidas[2])

# con esto reemplazamos un elemento en la lista

comidas[0] = "salsa"
print(comidas)

comidas[7][0] = "papas"
print(comidas)

# if, elif, else

haceFrio = False
haceCalor = False
comprateUnAire = True


if haceFrio:
    print("abrigate")
elif comprateUnAire:
    print("dale")
else:
    print("tomate una caipirinha")


# while, for

comida = ["lentejas", "arroz", "maiz"]

for food in comida:
    if food == "arroz":
        print("tengo arroz")
    print(food)


for number in range(5,24):
    print(number)

for numeros in range(7,101):
    if numeros % 2 == 0:
        print(numeros)

# while

count = 5

while count <= 10:
    print(count)
    count = count + 1


# ejercicio hola mundo

numerosDel10al0 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for numero in numerosDel10al0:
    if numero == 8:
        print("que emocion!")
    elif numero == 5:
        print("falta poco!!!")
    elif numero == 2:
        print("ya casi!!!!!!!1")
    elif numero == 0:
        print("Hola mundo!")
    else:
        print(numero)


# otra forma de resolver el ejercicio

for indice in range(11):
    numero = 10 - indice
    if numero == 8:
        print("que emocion!")
    elif numero == 5:
        print("falta poco!!!")
    elif numero == 2:
        print("ya casi!!!!!!!1")
    elif numero == 0:
        print("Hola mundo!")
    else:
        print(numero)



































