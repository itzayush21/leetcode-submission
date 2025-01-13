class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        max_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            max_matrix[i][i] = arr[i]
            for j in range(i + 1, n):
                max_matrix[i][j] = max(max_matrix[i][j - 1], arr[j])

        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                dp[start][end] = float('inf')
                for k in range(start, end):
                    cost = (
                        dp[start][k] +
                        dp[k + 1][end] +
                        max_matrix[start][k] * max_matrix[k + 1][end]
                    )
                    dp[start][end] = min(dp[start][end], cost)

        return dp[0][n - 1]
