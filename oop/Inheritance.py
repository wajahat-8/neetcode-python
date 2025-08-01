class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return f"{self.name} makes sound"

    def move(self):
        return f"{self.name} moves"

# single inheritance: Dog inherits from Animal

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name) # Call parent class's __init__
        self.breed=breed

    # Method overrriding

    def speak(self):
        return f"{self.name} barks"

    def fetch(self):
        return f"{self.name} fetches the ball"
# Another base class for multiple inheritance

class Swimmer:
    def __init__(self):
        self.swim_speed="moderate"

    def swim(self):
        return f"swims at {self.swim_speed} speed"

# Multiple inheritance: Dolphin inherits from Animal and Swimmer
class Dolphin(Animal,Swimmer):
    def __init__(self, name,species):
        super().__init__(name)
        Swimmer.__init__(self)
        self.species=species
    # Method overriding

    def speak(self):
        return f"{self.name} clicks and whistles"

    def swim(self):
        return f"{self.name} swims gracefully at {self.swim_speed} speed"
def main():

# Create instances
    dog=Dog("Buddy","Golden Retriver")
    dolphin=Dolphin("Flipper","Bottlensone")
 # Demonstrate method calls
    print("Dog behavior:")
    print(dog.speak()) # Overridden method
    print(dog.move())  # Inherited from Animal
    print(dog.fetch()) # Dog-specific method
    print(f"Breed: {dog.breed}\n")
    print("-------------|-----------")
    print("Dolphin behavior:")
    print(dolphin.speak())  # Overridden method
    print(dolphin.move())   # Inherited from Animal
    print(dolphin.swim())   # Overridden from swimmerSwimmer
    print(f"Species: {dolphin.species}\n")
      # Using isinstance() to check object type
    print("isinstance checks:")
    print(f"Is dog an Animal? {isinstance(dog, Animal)}")  # True
    print(f"Is dog a Dolphin? {isinstance(dog, Dolphin)}")  # False
    print(f"Is dolphin an Animal? {isinstance(dolphin, Animal)}")  # True
    print(f"Is dolphin a Swimmer? {isinstance(dolphin, Swimmer)}")  # True
    print(f"Is dolphin a Dog? {isinstance(dolphin, Dog)}")  # False

    # Using issubclass() to check class relationships
    print("\nissubclass checks:")
    print(f"Is Dog a subclass of Animal? {issubclass(Dog, Animal)}")  # True
    print(f"Is Dolphin a subclass of Animal? {issubclass(Dolphin, Animal)}")  # True
    print(f"Is Dolphin a subclass of Swimmer? {issubclass(Dolphin, Swimmer)}")  # True
    print(f"Is Dog a subclass of Swimmer? {issubclass(Dog, Swimmer)}")  # False
    print(f"Is Animal a subclass of Dog? {issubclass(Animal, Dog)}")  # False

main()