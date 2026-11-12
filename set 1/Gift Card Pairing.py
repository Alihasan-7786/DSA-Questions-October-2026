class Solution:
    def twoSum(self, prices, target):
        seen = {}
        for i in range(len(prices)):
            diff = target - prices[i]
            if diff in seen:
                return [seen[diff], i]
            seen[prices[i]] = i

n = int(input())
prices = list(map(int, input().split()))
target = int(input())

obj = Solution()
print(*obj.twoSum(prices, target))
