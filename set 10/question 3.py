class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        best_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if profit > best_profit:
                best_profit = profit
            if prices[i] < min_price:
                min_price = prices[i]

        return best_profit

n = int(input())
prices = list(map(int, input().split()))

obj = Solution()
print(obj.maxProfit(prices))