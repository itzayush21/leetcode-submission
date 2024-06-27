class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        c={}
        c1=0
        for num in time:
            r=num%60
            if r==0:
                if 0 in c:
                    c1+=c[0]
            elif (60-r) in c:
                c1+=c[60-r]
            if r in c:
                c[r]+=1
            else:
                c[r]=1

        return c1
        