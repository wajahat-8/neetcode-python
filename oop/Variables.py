class Dog:
    #class variable(shared by all instance)
    species="canis familiaris"

    def __init__(self,name ,age):
        # instance variable unique to each object
        self.name=name
        self.age=age
    def description(self):
        return f"{self.name} is {self.age} years old and belongs to {self.species}"
    # Method to modify instance variable
    def have_birthday(self):
        self.age+=1

    @classmethod
    def change_species(cls,new_species):
        cls.species=new_species
    @staticmethod
    def info():
        return "this is a dog class"
# create teo Dog instances
dog1=Dog("Buddy",3)
dog2=Dog("Max",5)

# access instance variables
print(dog1.name)
print(dog2.name)
#access class variable
print(dog1.species)
print(dog2.species)

# Modify instance variable
dog1.have_birthday()
print(dog1.description())
print(dog2.description())

# Modify class variable
Dog.change_species("canis lupus")
print(dog1.species)
print(dog2.species)
# calling static method
print(Dog.info())
