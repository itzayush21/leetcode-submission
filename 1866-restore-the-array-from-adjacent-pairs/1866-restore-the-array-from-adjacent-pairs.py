class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        d=defaultdict(list)
        res=[0]*(len(adjacentPairs)+1)
        for a,b in adjacentPairs:
            d[a].append(b)
            d[b].append(a)
        for key,value in d.items():
            if len(value)==1:
                res[0]=key
                res[1]=value[0]
                break
        for i in range(2,len(adjacentPairs)+1):
            v=d[res[i-1]]
            print(v)
            res[i]=v[0] if v[1]==res[i-2] else v[1]
        return res

        