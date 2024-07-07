class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=sorted(strs, key=len)
        res=""
        for i in range(len(s[0])):
            for num in s:
                if num[i]!=s[0][i]:
                    return res
            res+=s[0][i]
        return res
                
