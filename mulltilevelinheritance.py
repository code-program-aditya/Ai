class animal:
    def __init__(self, species):
        self.species = species
    def display_characteristics(self):
        print(f"Species: {self.species}")
        print("Animals are living organisms that can move and respond to their environment.")
class mammual(animal):
    def __init__(self, species, has_fur=True):
        super().__init__(species)
        self.has_fur = has_fur
    def display_characteristics(self):
        super().display_characteristics()
        print("Mammals are warm-blooded animals that have hair or fur and produce milk for their young.")
        print(f"Has Fur: {'Yes' if self.has_fur else 'No'}")
class dog(mammual):
    def __init__(self, breed, has_fur=True):
        super().__init__("Dog", has_fur)
        self.breed = breed
    def display_characteristics(self):
        super().display_characteristics()
        print(f"Breed: {self.breed}")
        print("dogs are loyal intelligent, and often kept as pets.")
# Example usage
dog1 = dog("german shepherd")
dog1.display_characteristics()