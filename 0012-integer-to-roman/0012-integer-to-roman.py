class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romans = [["I", 1],["IV", 4],["V", 5],["IX", 9],["X", 10],
    ["XL", 40],["L", 50],["XC", 90],["C", 100],["CD", 400],["D", 500],
    ["CM", 900],["M", 1000]]
        res=""
        for sym,val in reversed(romans):
            if num//val:
                c=num//val
                res+=(sym*c)
                num=num%val
        return res