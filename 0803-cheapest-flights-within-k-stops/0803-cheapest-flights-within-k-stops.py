class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        costs = [float("inf")] * n
        costs[src] = 0

        for i in range(k + 1):
            tmp = costs[:]
            for s, d, p in flights:
                if costs[s] == float("inf"):
                    continue
                if costs[s] + p < tmp[d]:
                    tmp[d] = costs[s] + p
            costs = tmp

        return -1 if costs[dst] == float("inf") else costs[dst]