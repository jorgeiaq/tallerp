if exercises == 1:
#ejercicio 1
base = float(input("ingrese la base del triangulo"))
height = float(input("ingrese la altura del triangulo"))
area = (base * height) / 2
print("el area del triangulo es:", area)

elif exercises == 2:
#ejercicio 2
num1 = float(input("ingrese un numero"))
num2 = float(input("ingrese otro numero"))
operation= num1 + num2
print("el resultado de la operacion es", num1, "y", num2, "es:", operation)

elif exercises == 3:
# ejercicio 3
num = float(input("ingrese un numero cualquiera"))
result = num ** 2
print("el resultado es", num, "es", result)

elif exercises == 4:
# ejercicio 4
addition = 1234 + 532
print("la suma da como resultado:", addition)

elif exercises == 5:
# ejercicio 5
subtraction = 1234 - 532
print("el resultado es:", subtraction)

elif exercises == 6:
# ejercicio 6
multiplication = 1234 * 532
print("el resultado es:", multiplication)

elif exercises == 7:
# ejercicio 7
division = 1234 / 532
print("la division da como resultado:", division)

elif exercises == 8:
# ejercicio 8
num1 = 1234
num2 = 532
module = num1 % num2
print("el modulo es:", module)

elif exercises == 9:
# 1 euro equivale 1,10 dolares
euro = float(input("ingrese la cantidad a convertir"))
dollar = 1.10
change = euro * dollar
print("su cambio es:", change)

elif exercises == 10:
# ejercicio 10
height = float(input("ingrese el valor"))
width = float(input("ingrese la anchura"))
area = height * width
print("el area del rectangulo es:" + str(area))

elif exercises == 11:
# ejercicio 11
side = float(input("el lado del cuadrado es"))
area = side ** 2
perimeter = 4 * side
print("el area del cuadrado es:", area)
print("el perimetro es:", perimeter)
print("el lado es:", side)

elif exercises == 12:
# ejercicio 12
import math
radio = float(input("ingrese el valor"))
height = float(input("ingrese el valor"))
volume = math.pi * radio**2 * height 
area = 2 * math.pi * radio * height + 2 * math.pi * radio**2
print("el volumen del cilindro es:", volume)
print("el area es:", area)

elif exercises == 13:
# ejercicio 13
import math
radio = float(input("ingrese el radio de la circunferencia"))
length = 2 * math.pi * radio 
area = math.pi * radio ** 2
enrolled_area =(math.pi * radio ** 2) / 2
print("el area es:", area)
print("la longitud:", length)
print("el area del circulo inscrito es:", enrolled_area)

elif exercises == 14:
# ejercicio 14
num1 = float(input("ingrese un numero"))
num2 = float(input("ingrese otro numero"))
num3 = float(input("ingrese otro numero"))
prom = (num1 + num2 +num3) / 3
print("el promedio de los numeros es:", prom)




