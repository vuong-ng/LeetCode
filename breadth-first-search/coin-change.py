class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        # min_cost = -1
        # cur_sum = 0
        if amount == 0:
            return 0
        def dfs(rem):
            min_cost = float('inf')
            if rem == 0:
                return 0
            if rem < 0:
                return -1
            if rem in memo:
                return memo[rem]
            for coin in coins:
                res = dfs(rem - coin)
                if res > -1:
                    min_cost = min(res + 1, min_cost)
            if min_cost > -1:
                memo[rem] = (min_cost)
            # if min_cost == float('inf'):
            #     memo[rem] = 0
            return memo[rem] if min_cost != float('inf') else -1
        return dfs(amount)