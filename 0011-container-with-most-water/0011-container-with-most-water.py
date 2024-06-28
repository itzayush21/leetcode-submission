class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        l,r=0,len(height)-1
        while(l<r):
            if height[r]>height[l]:
                area=max(min(height[l],height[r])*(r-l),area)
                l+=1
            if height[l]>=height[r]:
                area=max(min(height[l],height[r])*(r-l),area)
                r-=1
            '''if height[l]<=height[r]:
                area=max(min(height[l],height[r])*(r-l),area)
                l+=1'''
        return area
        