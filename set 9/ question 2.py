class Solution:
    def twoSum(self, prices, T):
        left = 0
        right = len(prices) - 1
        while left < right:
            total = prices[left] + prices[right]
            if total == T:
                return left + 1, right + 1
            elif total < T:
                left += 1
            else:
                right -= 1

        return -1, -1

n = int(input())
prices = list(map(int, input().split()))
T = int(input())

obj = Solution()
i, j = obj.twoSum(prices, T)

print(i, j)