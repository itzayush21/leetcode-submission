class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        l=0
        store,res=0,[]
        while len(s[l:])>store:
            res=[]
            for i in range(l,len(s)):
                if s[i] not in res:
                    res.append(s[i])
                else:
                    l+=1
                    break
            store=max(store,len(res))
        return store
        