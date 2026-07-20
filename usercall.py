from oops_proj import chatbook

user1 = chatbook()

user1.name = "John Doe"
print(user1.name)  # Output: John Doe

#How to access private attribute
print(user1._chatbook__name)  # Output: Default Name (accessing private attribute)

# Using getter and setter methods to access private attribute
print(user1.get_name())  # Output: Default Name (using getter method)
user1.set_name("Jane Smith")
print(user1.get_name())  # Output: Jane Smith (using getter method after setting new value)

# Using static methods to access and modify class variable
print("User ID:", user1.get_id())  # Output: User ID: 1 (using static method to get user ID)
chatbook.set_id(10)  # Using static method to set user ID
print("User ID after setting:", user1.get_id())  # Output: User ID after setting: 10 (using static method to get updated user ID)