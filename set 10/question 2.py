class Solution:
    def floorCeiling(self, prices, q):
        n = len(prices)
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if prices[mid] <= q:
                left = mid + 1
            else:
                right = mid
        floor_index = left - 1
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if prices[mid] < q:
                left = mid + 1
            else:
                right = mid
        ceiling_index = left

        floor_value = prices[floor_index] if floor_index >= 0 else "None"
        ceiling_value = prices[ceiling_index] if ceiling_index < n else "None"

        return floor_value, ceiling_value

n = int(input())
prices = list(map(int, input().split()))
q = int(input())

obj = Solution()
floor_value, ceiling_value = obj.floorCeiling(prices, q)

print(floor_value, ceiling_value)