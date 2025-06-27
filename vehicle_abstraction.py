from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"The {self.model} car's engine is starting with a roar!"

class Motorcycle(Vehicle):
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"The {self.model} motorcycle's engine is revving up!"

# Example 1: Using Car and Motorcycle objects
print("Example 1:")
car = Car("Toyota Corolla")
motorcycle = Motorcycle("Harley Davidson")
print(car.start_engine())
print(motorcycle.start_engine())

# Example 2: Attempting to instantiate the abstract class
print("\nExample 2:")
try:
    vehicle = Vehicle()  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

# Example 3: Using multiple vehicles
print("\nExample 3:")
vehicles = [Car("Honda Civic"), Motorcycle("Yamaha R1")]
for v in vehicles:
    print(v.start_engine())