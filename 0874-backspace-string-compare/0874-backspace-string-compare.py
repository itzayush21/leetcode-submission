class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1=[]
        stack2=[]
        for i in s:
            if i=='#' and stack1:
                stack1.pop()
                continue
            elif i!='#':
                stack1.append(i)
        for i in t:
            if i=='#' and stack2:
                stack2.pop()
                continue
            elif i!='#':
                stack2.append(i)
        return True if stack1==stack2 else False
        