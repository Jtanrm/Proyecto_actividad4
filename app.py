# Ejercicio 2:
# Escribe un programa que pida al usuario su nombre y apellido, 
# y luego los imprima juntos en un mensaje de saludo.

nombre = "Jhonatan"
apellido = "Rodriguez"
print("Hola mi nombre es : ", nombre, apellido)

# Ejercicio 2:
# Crea una variable llamada precio con el valor 100. 
# Calcula el precio con un descuento del 15% y muestra el precio final.

precio = "100"
descuento = 0.15
porcentaje = precio - (precio * descuento) 
print(f"El valor con decuento del 15% es de : {porcentaje}")

# Ejercicio 3:
# Escribe un programa que pida al usuario su edad y luego determine si es mayor o menor de edad.

edad = int(input("Por favor, ingresa tu edad : "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")



# Ejercicio 4:
# Crea un programa que pida al usuario un número y determine si es par o impar.

numero =int(input("Ingrese tú puto número:"))

if numero % 2 ==0:
 print(f"El número {numero} es par.")
else:
 print(f"Tu jodido número {numero} es impar pendejo")

# Ejercicio 5:

# Escribe un programa que pida al usuario dos números y luego calcule su suma, resta, multiplicación y división.

numero1 = int(input("Ingrece su primer número : "))
numero2 = int(input("Ingrece su  segundo número : "))

# Menú de opciones

print("\nseleccione el calculo a realizar:")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")

# Solicitamos al ususario que seleccione una opción.
opcion =input("Seleccione su opción requerida (1/2/3/4) : ")

# Realizar operación

if opcion == "1":
    resultado = numero1 + numero2
    operacion  = "suma"
elif opcion == "2":
    resultado = numero1 - numero2
    operacion = "resta"
elif opcion == "3":
    resultado = numero1 * numero2
    operacion = "multiplicación"
elif opcion == "4":
    if numero2 !=0:
       resultado = numero1 / numero2
       operacion ="division"
    else:
       resultado = "indefinida (division por cero no permitida )"
       operacion ="division"
else:
   resultado = "Opción no validad"
   operacion = None

#Mostrar el resultado de la operación

if operacion:
   print(f"\nEl resultado de la {operacion} de {numero1} y {numero2} es: {resultado}")
else:
   print(f"\n{resultado}")
   
# Ejercicio 6:

# Crea un programa que pida al usuario su calificación y luego imprima el mensaje "Aprobado" si la calificación es mayor o igual a 70, o "Reprobado" si la calificación es menor que 70.

nota1 = float(input("Por favor, ingrese la primera nota: "))
nota2 = float(input("Por favor, ingrese la segunda nota: "))
nota3 = float(input("Por favor, ingrese la tercera nota: "))

# Calcular promedio

promedio = (nota1 + nota2 + nota3)/3

# Determinamos si aprobo el promedio o no

if promedio >= 70:
    print(f"Aprobaste con un promedio de {promedio:.2f}")
else:
    print(f"Reprobo con un promedio de {promedio:.2f}")

# Ejercicio 7:

# Escribe un programa que pida al usuario dos números y luego determine cuál es el mayor.
num1 = int(input("Ingrezar # 1: "))
num2 = int(input("Ingrezar # 2: "))

#Determinar cual es mayor o menor

if num1 > num2:
    print(f"El número {num1} es mayor que {num2}.")
elif num2 > num1:
    print(f"El número {num2} es mayor de {num1}.")
else:
    print("Ambos número son iguales.")
    

# Ejercicio 8:

# Crea un programa que pida al usuario su nombre y luego imprima un mensaje de bienvenida con su nombre.


    nombre = input("Ingrece su Nombre: ")
print(f"¡Bienvenido,pendejo Alias {nombre}!")


# Ejercicio 9:

# Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar de ese número hasta el 10.

try:
    numero = int(input("Por favor, ingresa un número: "))
    
    # Imprimir la tabla de multiplicar del número ingresado
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")


# Ejercicio 10:

# Crea un programa que pida al usuario dos números y luego calcule su promedio.

numero1 = float(input("Ingrese un numero que desee: "))
numero2 = float(input("Ingrese otro numero que desee: "))

promedio = (numero1 + numero2) /2

print(f"El promedio de {numero1} y {numero2} es: {promedio}")



