class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]

        
        for i in range(len(coins) + 1):
            dp[i][0] = 0


        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):

                not_take=dp[i-1][j]

                take=float('inf')
                if coins[i-1]<=j:
                    take=1+dp[i][j-coins[i-1]]

                dp[i][j]=min(not_take,take)

        ans=dp[len(coins)][amount]

        if ans == float('inf'):
            return -1

        return ans


        # def helper(i,amt):

        #     if i==len(coins):
        #         return float('inf')

        #     if amt==0:
        #         return 0

        #     if (i,amt) in dp:
        #         return dp[(i,amt)]

        #     not_take=helper(i+1,amt)
            
        #     take=float('inf')
        #     if coins[i]<=amt:
        #         take=1+helper(i,amt-coins[i])

        #     dp[(i,amt)]=min(take,not_take)

        #     return dp[(i,amt)]

        # ans = helper(0, amount)

        # if ans == float('inf'):
        #     return -1

        # return ans
        