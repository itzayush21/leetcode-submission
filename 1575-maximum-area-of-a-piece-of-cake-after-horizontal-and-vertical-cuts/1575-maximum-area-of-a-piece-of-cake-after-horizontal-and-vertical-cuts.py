class Solution(object):
    def maxArea(self, h, w, hc, vc):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        hc.sort()
        vc.sort()
        maxh, maxv = max(hc[0], h - hc[-1]), max(vc[0], w - vc[-1])
        for i in range(len(hc)):
            maxh = max(maxh, hc[i] - hc[i-1])
        for i in range(len(vc)):
            maxv = max(maxv, vc[i] - vc[i-1])
        return (maxh * maxv) % 1000000007
       
   
       
        return area % (10**9 + 7)

        