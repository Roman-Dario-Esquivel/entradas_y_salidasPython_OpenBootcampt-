from pickle import *

class Vehiculo:

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return "el auto es de color "+ self.color + ", tiene "+ self.puertas +" puertas"


chevy = Vehiculo("negro mate", "2")
print(chevy)

file = open('vehiculo_objeto', 'w+b')

dump(chevy, file)

file.seek(0)
nuevo_chevy = load(file)

print(nuevo_chevy)
file.close()