import random

# Base class for all superheroes
class Superhero:
    """
    A class representing a superhero with core attributes and methods.
    """
    def __init__(self, name, secret_identity, powers, health):
        """
        Constructor to initialize a new Superhero object.
        
        Args:
            name (str): The superhero's public name.
            secret_identity (str): The superhero's civilian identity.
            powers (list): A list of the superhero's abilities.
            health (int): The superhero's health points.
        """
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
        self.health = health
        self.is_active = True

    def display_info(self):
        """
        Prints the superhero's key information.
        """
        print(f"Name: {self.name}")
        print(f"Secret Identity: {self.secret_identity}")
        print(f"Powers: {', '.join(self.powers)}")
        print(f"Health: {self.health}")
        print("-" * 20)

    def fight(self, enemy):
        """
        A method to simulate a fight with an enemy.
        """
        print(f"{self.name} is fighting {enemy}!")
        damage = random.randint(10, 50)
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Current health: {self.health}")
        if self.health <= 0:
            self.is_active = False
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} survives the attack.")

# Inherited class for flying superheroes
class FlyingSuperhero(Superhero):
    """
    A specialized class for superheroes who can fly.
    Inherits from the Superhero class.
    """
    def __init__(self, name, secret_identity, powers, health, flight_speed):
        """
        Constructor for a flying superhero, calling the parent's constructor
        and adding a new attribute.
        """
        # Call the parent class's constructor
        super().__init__(name, secret_identity, powers, health)
        self.flight_speed = flight_speed
        # Add a flying-specific power if not already present
        if "flight" not in [p.lower() for p in self.powers]:
            self.powers.append("Flight")

    def fly(self):
        """
        A method specific to flying superheroes.
        """
        if self.is_active:
            print(f"{self.name} is soaring through the sky at {self.flight_speed} mph! ✈️")
        else:
            print(f"{self.name} is unable to fly right now.")

# --- Main Program Execution ---
if __name__ == "__main__":
    print("--- Activity 1: Superhero Class ---")
    
    # Create an instance of the Superhero class
    hero1 = Superhero("Captain Courage", "John Smith", ["Super Strength", "Invulnerability"], 100)
    hero1.display_info()
    hero1.fight("Dr. Doom")

    print("\n--- Inheritance in action ---")
    # Create an instance of the FlyingSuperhero class
    flying_hero = FlyingSuperhero("Sky Blazer", "Jane Doe", ["Super Speed"], 120, 500)
    flying_hero.display_info()
    flying_hero.fly()
    flying_hero.fight("The Abomination")
    flying_hero.fly()

