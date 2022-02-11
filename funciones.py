# def imprimir_mensaje():
#     print("Este es un mensaje especial")
#     print("¡Estoy aprendiendo a programar!")

def conversacion(opcion):
    print("Hola")
    print("¿Cómo estás?")
    print(f"Elegiste la opción {opcion}")
    print("¡Adios!")


opcion = input("Elige una opción (1,2,3):")

if opcion == "1":
    conversacion(opcion)
elif opcion == "2":
    conversacion(opcion)
elif opcion == "3":
    conversacion(opcion)
else:
    print("Elige la opción correcta")
