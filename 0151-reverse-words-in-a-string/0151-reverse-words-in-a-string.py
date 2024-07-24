class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            else:
                j = i
                while j < len(s) and s[j] != " ":
                    j += 1
                w = s[i:j]
                if res != '':
                    res = w + " " + res
                else:
                    res = w
                i = j
        
        return res
            


            