class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total=numBottles
        while numBottles>=numExchange:
            total+=numBottles/numExchange
            numBottles=numBottles/numExchange + numBottles%numExchange

        return total
        