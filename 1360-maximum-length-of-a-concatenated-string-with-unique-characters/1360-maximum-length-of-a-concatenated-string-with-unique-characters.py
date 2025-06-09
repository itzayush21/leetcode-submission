class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        maxlen = 0
        unique = [""]

        def isvalid(s):
            return len(s) == len(set(s))

        for word in arr:
            for j in unique:
                tmp = word + j
                if isvalid(tmp):
                    unique.append(tmp)
                    maxlen = max(maxlen, len(tmp))

        return maxlen
            