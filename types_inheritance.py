# #Single or basic inheritance

# class Parent:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         return f"Hello, my name is {self.name}"
    
# class Child(Parent):
#     def play(self):
#         return f"{self.name} is playing."
    
# child = Child("Alice")
# print(child.greet())  # Output: Hello, my name is Alice
# print(child.play())   # Output: Alice is playing.


# #multilevel inheritance
# class GrandParent:
#     def __init__(self, grandparent_attribute):
#         self.grandparent_attribute = grandparent_attribute

#     def grandparent_method(self):
#         return f"This is a method from the GrandParent class: {self.grandparent_attribute}"

# class Parent(GrandParent):
#     def __init__(self, grandparent_attribute, parent_attribute):
#         super().__init__(grandparent_attribute)
#         self.parent_attribute = parent_attribute

#     def parent_method(self):
#         return f"This is a method from the Parent class: {self.parent_attribute}"

# class Child(Parent):
#     def __init__(self, grandparent_attribute, parent_attribute, child_attribute):
#         super().__init__(grandparent_attribute, parent_attribute)
#         self.child_attribute = child_attribute

#     def child_method(self):
#         return f"This is a method from the Child class: {self.child_attribute}"

# # Example usage
# child = Child("Grandparent Value", "Parent Value", "Child Value")
# print(child.grandparent_method())  # Output: This is a method from the GrandParent class: Grandparent Value
# print(child.parent_method())       # Output: This is a method from the Parent class: Parent Value
# print(child.child_method())        # Output: This is a method from the Child class: Child Value


# #hierarchical inheritance

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hello, my name is {self.name}"
    
# class Child1(Parent):
#     def play(self):
#         return f"{self.name} is playing."

# class Child2(Parent):
#     def study(self):
#         return f"{self.name} is studying."      
    
# child1 = Child1("Alice")
# print(child1.greet())  # Output: Hello, my name is Alice 
# print(child1.play())   # Output: Alice is playing.   
# child2 = Child2("Bob")
# print(child2.greet())  # Output: Hello, my name is Bob
# print(child2.study())  # Output: Bob is studying.


# #Multiple/Diamond inheritance

# class A:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"Hello from A, my name is {self.name}")

# class B(A):
#     def greet(self):
#         print(f"Hello from B, my name is {self.name}")
#         super().greet()  # Call the greet method of the base class
# class C(A):
#     def greet(self):
#         print(f"Hello from C, my name is {self.name}")
#         super().greet()  # Call the greet method of the base class

# class D(B, C):
#     def greet(self):
#         print(f"Hello from D, my name is {self.name}")
#         super().greet()  # Call the greet method of the base class


# d = D("Diamond")
# d.greet()


#Hybrid inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

#Intermediate class 1(hierarchical inheritance)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding its young.")

#Intermediate class 2(multiple inheritance)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

#Derived class (multiple inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)

    def nocturnal(self):
        print(f"{self.name} is a nocturnal bat.")


bat = Bat("Bruce")
bat.speak()  # Output: Bruce is a bat with black fur.   
bat.feed()   # Output: Bruce is feeding its young.
bat.fly()    # Output: Bruce is flying. 
bat.nocturnal()  # Output: Bruce is a nocturnal bat.
