class Dog:
  def bark(self):
    print(self.name)

my_dog = Dog()
my_dog.name = "Fido"

other_dog = Dog()
other_dog.name = "Sara"

my_dog.bark()