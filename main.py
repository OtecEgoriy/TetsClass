class Car():
  def __init__(self, name, color, year):
    self.name = name
    self.color = color
    self.year = year

  def drive (self):
    print('Car driving')

opel_car = Car('Opel','Blue','1993')
opel_car.drive()
print(opel_car.name)
print(opel_car.color)
print(opel_car.year)
