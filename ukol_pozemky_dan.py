# UKOL 1
from math import ceil

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    ESTATE_COEFFICIENTS = {
        'land': 0.85,
        'building site': 9,
        'forrest': 0.35,
        'garden': 2
    }

    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        coefficient = self.ESTATE_COEFFICIENTS.get(self.estate_type, 0)
        tax = self.area * coefficient * self.locality.locality_coefficient
        return ceil(tax)

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
            tax *= 2
        return ceil(tax)
    
lokalita = Locality("Lokalita s koeficientem 2", 2)
estate1 = Estate(lokalita, 'forrest', 500)
print(f"Daň za lesní pozemek: {estate1.calculate_tax()}")

manetin = Locality("Manětín", 0.8)
estate2 = Estate(manetin, 'land', 900)
print(f"Daň za zemědělský pozemek: {estate2.calculate_tax()}")

residence1 = Residence(manetin, 120, False)
print(f"Daň za dům: {residence1.calculate_tax()}")

brno = Locality("Brno", 3)
residence2 = Residence(brno, 90, True)
print(f"Daň za kancelář: {residence2.calculate_tax()}")