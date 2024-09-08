# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

def single_inheritance_demo():
    print("Single Inheritance Demo:")
    dog = Dog("Dog")
    print(dog.speak())

# Multiple Inheritance
class Walker:
    def walk(self):
        return "Walking"

class Swimmer:
    def swim(self):
        return "Swimming"

class Amphibian(Walker, Swimmer):
    def display_abilities(self):
        return f"Abilities: {self.walk()} and {self.swim()}"

def multiple_inheritance_demo():
    print("\nMultiple Inheritance Demo:")
    amphibian = Amphibian()
    print(amphibian.display_abilities())

if __name__ == "__main__":
    single_inheritance_demo()
    multiple_inheritance_demo()
