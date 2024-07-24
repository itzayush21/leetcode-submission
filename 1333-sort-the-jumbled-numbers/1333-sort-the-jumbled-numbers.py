class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d=[]
        for i in nums:
            i=str(i)
            res=""
            for j in i:
                res+=str(mapping[int(j)])
            d.append((int(i),int(res)))
        result = [j for j, k in sorted(d, key=lambda x: x[1])]

        print(result)
        return result
