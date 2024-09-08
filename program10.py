class Dog:
    # Constructor to initialize the attributes
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Method to display information about the dog
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")

    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} says woof!")


def main():
    # Create an object of the Dog class
    dog1 = Dog("Buddy", "Labrador Retriever")

    # Access and display data members using object
    print("Accessing data members:")
    print("Dog name:", dog1.name)
    print("Dog breed:", dog1.breed)

    # Call methods using object
    print("\nCalling methods:")
    dog1.display_info()
    dog1.bark()


if __name__ == "__main__":
    main()
