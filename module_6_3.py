class Vehicle:
    def __init__(self):
        vehicle_type = "none"
class Car:
    def __init__(self, power):
        self.price = 1_000_000
        self.power = power

    def get_horse_powers(self):
        return self.power

class Nissan(Vehicle, Car):
    def __init__(self, power, vehicle_type, price):
        Car.__init__(self, power)
        self.vehicle_type = vehicle_type
        self.price = price

    def horse_powers(self):
        super().powers(self)

a = Car(80)
b = Nissan(120,'Rotor', 1_500_000)

print(b.vehicle_type)
print(b.price)
print(a.get_horse_powers())
print(b.get_horse_powers())