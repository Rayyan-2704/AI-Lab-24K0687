class Vehicle:
    def __init__(self, vehicle_id, brand, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rent_per_day = rent_per_day

    def display_details(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Brand: {self.brand}")
        print(f"Rent Per Day: ${self.rent_per_day:.2f}")

    def calculate_rent(self, days):
        return self.rent_per_day * days

def main():
    v1 = Vehicle("V-1001", "Pagani Zonda", 5750.25)
    v2 = Vehicle("V-1002", "Mercedes-Benz SLR", 6800.50)

    print("------------ Printing Details of Vehicle 1 ------------")
    v1.display_details()
    print(f"Total rent cost of vehicle 1 for 7 days: ${v1.calculate_rent(7):.2f}")

    print("\n------------ Printing Details of Vehicle 2 ------------")
    v2.display_details()
    print(f"Total rent cost of vehicle 2 for 4 days: ${v2.calculate_rent(4):.2f}")

main()