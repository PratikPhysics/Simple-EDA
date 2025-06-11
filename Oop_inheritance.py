# Base class representing a generic vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        # Initialize common attributes for all vehicles
        self.brand = brand
        self.model = model
        self.year = year

    # Method to start the engine
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

    # Method to stop the engine
    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped.")

# Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        # Call the constructor of the base class (Vehicle)
        super().__init__(brand, model, year)
        # Add an additional attribute specific to cars
        self.fuel_type = fuel_type

    # Method specific to Car
    def honk(self):
        print(f"{self.brand} {self.model} says Beep Beep!")

# Truck class inherits from Vehicle
class Truck(Vehicle):
    def __init__(self, brand, model, year, cargo_capacity):
        # Call the constructor of the base class (Vehicle)
        super().__init__(brand, model, year)
        # Add an additional attribute specific to trucks
        self.cargo_capacity = cargo_capacity

    # Method specific to Truck
    def load_cargo(self):
        print(f"Loading {self.cargo_capacity} tons of cargo into {self.brand} {self.model}.")

# Create an object of Car
my_car = Car("Toyota", "Corolla", 2022, "Petrol")

# Create an object of Truck
my_truck = Truck("Volvo", "FH16", 2020, 25)

# --- Using methods ---

# Start car engine (inherited from Vehicle)
my_car.start_engine()

# Honk the car horn (specific to Car)
my_car.honk()

# Start truck engine (inherited from Vehicle)
my_truck.start_engine()

# Load cargo into truck (specific to Truck)
my_truck.load_cargo()
