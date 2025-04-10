# pet.py

# Define the Pet class
class Pet:
    def __init__(self, kind, breed, name):
        # Initialize the pet's attributes (kind, breed, name)
        self._kind = kind
        self._breed = breed
        self._name = name

    # Getter methods
    def get_kind(self):
        return self._kind

    def get_breed(self):
        return self._breed

    def get_name(self):
        return self._name

    # Setter methods
    def set_kind(self, kind):
        self._kind = kind

    def set_breed(self, breed):
        self._breed = breed

    def set_name(self, name):
        self._name = name

    # Method to print pet details
    def print_details(self):
        print(f"Pet Name: {self._name}, Kind: {self._kind}, Breed: {self._breed}")


# Create instances of the Pet class
pet1 = Pet("Dog", "Labrador", "Buddy")
pet2 = Pet("Cat", "Siamese", "Whiskers")
pet3 = Pet("Bird", "Parrot", "Polly")

# Call the print_details method for each object
pet1.print_details()
pet2.print_details()
pet3.print_details()

# Demonstrate a special function: getattr()
# This function accesses an attribute dynamically
print("\nUsing getattr to access attributes:")
print(f"{pet1.get_name()}'s breed (via getattr):", getattr(pet1, "_breed"))
print(f"{pet2.get_name()}'s kind (via getattr):", getattr(pet2, "_kind"))
print(f"{pet3.get_name()}'s name (via getattr):", getattr(pet3, "_name"))
