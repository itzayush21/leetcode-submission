class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = [0] * n

        friendCount = n
        fp = 0  

        while friendCount > 1:
            for i in range(k):
                while friends[fp % n]:
                    fp += 1 
                fp +=1 
            friends[(fp - 1)%n] = 1
            friendCount -= 1

        fp = 0
        while friends[fp]:
            fp += 1

        return fp + 1