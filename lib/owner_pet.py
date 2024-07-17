class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self._owner = None
        self.owner = owner  # This will call the owner setter and update the owner's pet list
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if new_owner is not None and not isinstance(new_owner, Owner):
            raise Exception("The owner must be an instance of the Owner class")
        if self._owner is not new_owner:
            if self._owner is not None:
                self._owner._pets.remove(self)  # Remove pet from current owner
            self._owner = new_owner
            if new_owner is not None:
                new_owner._pets.append(self)  # Add pet to new owner's pet list


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class")
        if pet not in self._pets:
            pet.owner = self

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

# Testing the implementation

# Example usage:

# Create an owner
owner1 = Owner("John")

# Create pets
pet1 = Pet("Buddy", "dog")
pet2 = Pet("Mittens", "cat")
pet3 = Pet("Charlie", "bird")

# Add pets to owner
owner1.add_pet(pet1)
owner1.add_pet(pet2)
owner1.add_pet(pet3)

# Get owner's pets
print([pet.name for pet in owner1.pets()])  # ['Buddy', 'Mittens', 'Charlie']

# Get sorted pets by name
print([pet.name for pet in owner1.get_sorted_pets()])  # ['Buddy', 'Charlie', 'Mittens']
