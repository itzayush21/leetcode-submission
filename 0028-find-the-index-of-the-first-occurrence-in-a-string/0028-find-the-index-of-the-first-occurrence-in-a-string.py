class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        k=needle[0]
        check=""
        for i in range(len(haystack)):
            if haystack[i]==k:
                if(i+len(needle)<=len(haystack)):
                    check=haystack[i:i+len(needle)]
                    print(check)
                    if check == needle:
                        return i
        return -1

