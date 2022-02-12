from datetime import date


print('hola desde un archivo')

print("Today's date is: " + str(date.today()))

print("Bienvenido al programa de bienvenida")
edad = input("Introduzca su edad ")
print("tu edad es: " + edad)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))

# katas


print("Today's date is: " + str(date.today()))

parsec = int(input("ingrese los Pársec: "))

lightyears = 3.26156 * parsec

print(str(parsec) + " parsec, is " + str(lightyears) + " lightyears")
