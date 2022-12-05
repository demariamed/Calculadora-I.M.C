# Calculadora de Índice de masa corporal
# Aspirante: Consuelo de Maria Sanchez Medina
# C3 U Campers Python 
# Modulo 1

nombre = input("Introduce tu nombre:")
apellido = input("Introduce tu apellido paterno:")
apeliido = input("Introduce tu apellido materno:")
edad = int(input("Introduce tu edad en años:"))
peso = float(input("Introduce tu peso en kilogramos:"))
estatura = float(input("Introduce tu estatura en metros:")) 

IMC = peso / estatura **2
print("IMC: " + str(IMC))

if IMC >= 18.50 and IMC <= 24.99:
    print ("Todavia tienes chance de un pambazo más")
if IMC >= 25.00 and IMC <= 29.99:
    print ("Hay que bajarle a las garnachitas")
if IMC >= 30.00 and IMC <= 34.99:
    print ("Bueno, ¿Qué tu no entiendes?")

# Rubricas de IMC para referencias serias

# 18.50 - 24.99 Normal
# 25.00 - 29.99 Sobrepeso
# 30.00 - 34.99 Obesidad leve