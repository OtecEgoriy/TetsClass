class Car():
  def __init__(self, name, color, year):
    self.name = name
    self.color = color
    self.year = year
    print('Add Car')

  def drive (self):
    print(self.name + 'Car driving')

  def change_color (self, new_color):
        self.color = new_color
#Передаем методы класса предка
class Car_2(Car):
  def __init__(self, name, color, year):
    Car.__init__(self, name, color, year)
    print('Add Car_2')

man_car = Car_2 ('Man','Blue','1939')
