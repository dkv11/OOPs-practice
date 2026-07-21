# #Simple Inheritance

# #base class
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} makes a sound.")

# #derived class
# class Dog(Animal):
#     # #constructor overriding
#     # def __init__(self):
#     #     self.behavior = "friendly"

#     def speak(self):
#         print(f"{self.name} barks. He is {self.behavior}.")

# #create instance of base class
# animal = Animal("Generic Animal")
# animal.speak()  # Output: Generic Animal makes a sound.

# #create instance of derived class
# dog = Dog("Buddy")
# dog.speak()  # Output: Buddy barks.



#super keyword
class Animal:
    def __init__(self):
        self.name = "buddy"
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self,breed):
        super().__init__()  # Call the constructor of the base class
        self.breed = breed

    def speak(self):
        super().speak()  # Call the speak method of the base class
        print(f"{self.name} barks. He is {self.breed}.")

dog = Dog("Golden Retriever")
dog.speak()  # Output: Buddy makes a sound. Buddy barks. He is


