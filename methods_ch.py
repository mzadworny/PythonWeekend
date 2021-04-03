from datetime import datetime

class Car:
  def age(self):
    print(datetime.today().year - self.year)

my_whip = Car()
my_whip.year = 2005
my_whip.age()