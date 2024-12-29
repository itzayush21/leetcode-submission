class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for c in num:
            while k>0 and stack and stack[-1]>c:
                k-=1
                stack.pop()
            stack.append(c)
        res="".join(stack[:len(stack)-k])
        return str(int(res)) if res else "0"
        