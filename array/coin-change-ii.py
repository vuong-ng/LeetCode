class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # top-down 
        memo = {}
        
        def dp(i, remains):
            if remains == 0:
                return 1
            if i > len(coins)-1:
                return 0
            if (i, remains) in memo:
                return memo[(i,remains)]
            if remains - coins[i] < 0:
                memo[(i, remains)] = dp(i+1, remains)
            else:
                memo[(i,remains)] = dp(i, remains-coins[i]) + dp(i+1, remains)
            return memo[(i, remains)]

        return dp(0, amount)
        









        # memo = [[0] * (amount+1) for _ in range(len(coins)+1)]
        # for i in range(len(coins)):
        #     memo[i][0] = 1
        # print(memo)
        # for i in range(len(coins)-1 , -1, -1):
        #     for a in range(1, amount+1):
        #         remains = a-coins[i]

        #         if remains < 0:
        #             memo[i][a] = memo[i+1][a]

        #         else:
        #             memo[i][a] = memo[i][remains] + memo[i+1][a]
        # print(memo)
        # return memo[0][amount]