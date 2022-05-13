"""Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no. """

class alumno:
    """
    Esta es una clase donde se agregan todos los datos
    respecto a un alumno
    """
    def __init__(self, nombre, nota):
        # Todo lo que definamos en __init__ se corre
        # al crear una instancia de la clase
        self.nombre = nombre
        self.nota = nota
    def resultado(self):
        if (self.nota >= 5):
            print(f"El alumno ha APROBADO.")
        else:
            print(f"El alumno ha SUSPENDIDO. \nSuerte la próxima! :)")
    def imprimir(self):
        print(f"El nombre es {self.nombre} y su nota es {self.nota}")



# Creamos un objeto p1 que es una instancia de la clase Persona
alumno_1 = alumno("Marta", 4.9)  # Prueba para ver si suspende con el 4.9
alumno_2 = alumno("Joaquin", 9) # Comprueba que el alumno ha aprobado

alumno_1.imprimir()
alumno_1.resultado()

print("\n")

alumno_2.imprimir()
alumno_2.resultado()



