class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i,j,w=0,0,""
        res=""
        while i<len(s):
            if s[i]==" ":
                i+=1
                continue
            else:
                if s[i]!=" ":
                    j=i
                    while j<len(s) and s[j]!=" ":
                        j+=1
                w=s[i:j]
                print(w)
                if res != '':
                    res = w + " " + res
                else:
                    res = w
                print(res)
                i=j
        return(res)
            
        