class User:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def greet(self):
        print(f"Hello, {self.name}!")
        print(f"You're {self.age} years old and from {self.country}.")

# --- INTERACTIVE INPUT ---
name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

# Create a User object
user1 = User(name, age, country)

# Call a method to greet the user
user1.greet()
