import random
import string


class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool
    
    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric
    
    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        print('prices ', tax_percentage , self.catalogue_price)
        # compute the payable tax
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")    
        print(f"Catalogue Price: {self.catalogue_price}")    
        print(f"Payable tax: {self.compute_tax()}")         
    
        
    
class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo
    
    def __init__(self, id, license_plate, info) -> None:
        self.id = id
        self.license_plate = license_plate
        self.info = info
        
    def print(self):
        print("\n Registration complete. Vehicle information:")
        print("============================================")
        print(f"Id: {self.id}")    
        self.info.print()
     
    

class vehicleRegistry:
    vehicle_info = {}
    def __init__(self) -> None:
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("BMW 5", False, 35000)
        self.add_vehicle_info("Volkswagen ID3", True, 45000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)
        
    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    
    def generate_vehicle_licence(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"
    
    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_licence(vehicle_id)
        return Vehicle(id, license_plate, self.vehicle_info[brand])
        
    
class Application:
    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = vehicleRegistry()
        
        # create a vehicle
        vehicle = registry.create_vehicle(brand=brand)

        # print the vehicle registration information
        vehicle.print()
       
        
app = Application()
app.register_vehicle("BMW 5")
app.register_vehicle("Tesla Model 3")
app.register_vehicle("Volkswagen ID3")
        