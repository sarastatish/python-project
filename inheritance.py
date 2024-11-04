class animal:
    def speak(self):
        print("Animal is speaking")

        #child class
class Dog(animal):
    def bark(self):
      print("Dog is barking")

      a = animal()


      b = Dog()
      b.speak()
      b.bark()