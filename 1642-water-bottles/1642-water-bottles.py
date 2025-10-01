class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunkWater = 0
        rem = 0

        while numBottles > 0:
            drunkWater += numBottles
            exchangedWater = int((numBottles + rem) / numExchange)
            rem = (numBottles + rem) % numExchange
            numBottles = exchangedWater

        return drunkWater
