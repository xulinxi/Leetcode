# 1603. Design Parking System
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        
        self.parking_spots = [big, medium, small]
        
    # Need to understand the relationship between indices of parking spots related the numbers for carType
    # cartype = parking_spots index + 1
    def addCar(self, carType: int) -> bool:
        self.parking_spots[carType-1] -= 1
        # if self.parking_spots[carType-1] >= 0:
        #     return true
        return self.parking_spots[carType-1] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
