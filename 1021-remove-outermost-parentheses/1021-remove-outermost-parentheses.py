class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        open=0
        res=[]

        for i in s:
            if i=='(':

                if open>0:
                    res.append(i)

                open+=1
            else:

                open-=1
                if open>0:
                    res.append(i)

        return "".join(res)


        