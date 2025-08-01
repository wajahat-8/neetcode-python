class Student:
    def __init__(self,name ,age,grade):
            self.name=name #public
            self._school="High Scholl" #protected (by convention)
            self.__grade=grade # private (name mangled)
            self._age=age # protected with property access
    # --- Getter for grade (read-only) ---
    @property
    def grade(self):
          return self.__grade

    # --- Getter for age ---

    @property
    def age(self):
          return self._age

     # --- Setter for age with validation ---
    @age.setter
    def age(self,new_age):
          if new_age<5:
                raise ValueError("Age must me 5 or older.")
          self._age=new_age

    # --- Public method accessing protected/private data ---
    def show_info(self):
        print(f"Name: {self.name}")          # public
        print(f"School: {self._school}")     # protected
        print(f"Grade: {self.__grade}")      # private
        print(f"Age: {self.age}")            # protected via property

student=Student("Ali",15,"A")
print("--- Public Access ---")
print(student.name)
print("\n--- Protected Access (Not recommended directly) Works ---")
print(student._school)
print("\n--- Private Access (Fails directly) ---")
try:
      print(student.__grade)
except AttributeError as e:
      print("Error",e)
print("\n--- Accessing private via getter ---")
print(student.grade)

print("\n--- Using public method to access everything ---")
student.show_info()
print("\n--- Setting age (valid) ---")
student.age=18
print(student.age)

print("\n--- Setting age (invalid) ---")
try:
      student.age=3
except ValueError as e:
      print("error",e)

print("\n--- Accessing mangled private variable directly (not recommended) ---")
print(student._Student__grade)
