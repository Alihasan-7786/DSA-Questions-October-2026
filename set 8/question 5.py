class Solution:
    def shipWithinDays(self, weights, D):
        lo = 0
        hi = 0
        for w in weights:
            if w > lo:
                lo = w
            hi += w
        while lo < hi:
            mid = lo + (hi - lo) // 2
            days = 1
            current = 0
            for w in weights:
                if current + w > mid:
                    days += 1
                    current = w
                else:
                    current += w
            if days <= D:
                hi = mid
            else:
                lo = mid + 1

        return lo

n, D = map(int, input().split())
weights = list(map(int, input().split()))

obj = Solution()
print(obj.shipWithinDays(weights, D))