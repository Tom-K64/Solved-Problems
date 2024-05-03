"""
Problem Link:
https://leetcode.com/problems/design-parking-system/
"""

class ParkingSystem:

    def __init__(self, big, medium, small):
        self.big_limit = big
        self.medium_limit = medium
        self.small_limit = small
        self.parking_array = [None] * (big + medium + small)

    def addCar(self, carType):
        if carType == 1:
            limit = self.big_limit
        elif carType == 2:
            limit = self.medium_limit
        else:
            limit = self.small_limit
        count = 0
        for i in range(len(self.parking_array)):
            if self.parking_array[i] == carType:
                count += 1
            if count == limit:
                return False
            if self.parking_array[i] is None:
                self.parking_array[i] = carType
                return True
        return False
