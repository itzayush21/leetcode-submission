class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        name=[]
        res= zip(names, heights)
        s = sorted(res, key=lambda x: x[1], reverse=True)
        for i,j in s:
            name.append(i)
        return name
