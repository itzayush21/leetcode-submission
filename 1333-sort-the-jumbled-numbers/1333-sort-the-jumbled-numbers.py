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
        sorted_list=sorted(d, key=lambda x: x[1])
        result=[]
        for j,k in sorted_list:
            result.append(j)
        print(result)
        return result
