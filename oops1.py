class Employee:
    #special method to initialize the object
    def __init__(self):
        print("Employee object is created")
        self.id = 123
        self.salary = 50000
        self.designation = "Software Engineer"
        print("attributes are initialized")

    def travel(self, destination):
        print("this is a method of Employee class")
        print(f"Employee is traveling to {destination}")

# Creating an object of the Employee class
sam = Employee()

print(sam.salary)  # Output: 50000
print(sam.designation)  # Output: Software Engineer
sam.travel("New York")  # Output: Employee is traveling to New York

print(type(sam))  # Output: <class '__main__.Employee'>