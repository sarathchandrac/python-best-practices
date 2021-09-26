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
    
