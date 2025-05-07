class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        edges=defaultdict(list)
        for u,v,w in times:
            edges[u].append([v,w])

        minheap=[(0,k)]
        visit=set()
        t=0
        while minheap:
            w1,n1=heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            t=max(t,w1)

            for x,y in edges[n1]:
                if x not in visit:
                    heapq.heappush(minheap,(w1+y,x))
            
        return t if len(visit)==n else -1
        
        