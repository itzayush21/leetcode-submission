class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        N = len(s)
        j, i = 0, 0
        result = []
        res = ""
        while (j < N):
            res += s[j]
            if (len(res) == k):
                result.append(res)
                res = ""

            j += 1

        if (res != ""):
            while (len(res) < k):
                res += fill

            result.append(res)

        return result
            