class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        heap=[]
        for i in range(len(heights)-1):
            dist=heights[i+1]-heights[i]
            if dist<0:
                continue
            
            heapq.heappush(heap,-dist)
            bricks-=dist


            if bricks<0:
                if ladders==0:
                    return i
                ladders-=1
                bricks+=-heapq.heappop(heap)

        return len(heights)-1
