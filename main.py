class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print("Starting engine...")
        self.engine_on = True

    def make_noise(self):
        print("Beep beep!")

class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargo = True

class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("Vroom vroom!")

bikes = [Motorcycle("Harley-Davidson", 1000, 5000, 120),
         Motorcycle("Honda", 2000, 7000, 140),
         Motorcycle("Kawasaki", 3000, 8000, 160)]

trucks = [Truck("Ford", 10000, 20000),
          Truck("Chevy", 20000, 25000),
          Truck("Dodge", 30000, 30000)]

vehicles_to_compare = []

def display_vehicles(collection):
    for vehicle in collection:
        print(f"{vehicle.make} - {vehicle.miles} miles - ${vehicle.price}")
        vehicle.make_noise()

def add_vehicle_to_compare():
    selection = int(input("Enter the number of the vehicle you would like to compare: "))
    if selection > 0 and selection <= len(bikes) + len(trucks):
        if selection <= len(bikes):
            vehicle = bikes.pop(selection - 1)
        else:
            vehicle = trucks.pop(selection - len(bikes) - 1)
        vehicles_to_compare.append(vehicle)
    else:
        print("Invalid selection. Please try again.")
        add_vehicle_to_compare()

while True:
    print("1. Motorcycles")
    print("2. Trucks")
    print("3. Compare vehicles")
    selection = int(input("Enter the number of the category you would like to view: "))
    if selection == 1:
        display_vehicles(bikes)
    elif selection == 2:
        display_vehicles(trucks)
    elif selection == 3:
        while True:
            print("1. Add vehicle to compare")
            print("2. View vehicles to compare")
            print("3. Back to categories")
            inner_selection = int(input("Enter the number of your choice: "))
            if inner_selection == 1:
                add_vehicle_to_compare()
            elif inner_selection == 2:
                display_vehicles(vehicles_to_compare)
            elif inner_selection == 3:
                break
            else:
                print("Invalid selection. Please try again.")
    else:
        print("Invalid selection. Please try again.")
