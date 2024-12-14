class Vehicle:
    """
    A base class representing a generic vehicle.
    """
    def move(self):
        raise NotImplementedError("Subclasses must implement the move method.")

class Car(Vehicle):
    """
    A class representing a car.
    """
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    """
    A class representing a plane.
    """
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    """
    A class representing a boat.
    """
    def move(self):
        return "Sailing ⛵"

# Example usage
if __name__ == "__main__":
    # Create instances of each vehicle
    car = Car()
    plane = Plane()
    boat = Boat()

    # Demonstrate polymorphism
    vehicles = [car, plane, boat]
    for vehicle in vehicles:
        print(f"This vehicle is: {vehicle.move()}")
