class Solution:
    def floorSqrt(self, x):
        lo = 0
        hi = x
        answer = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid * mid <= x:
                answer = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return answer

x = int(input())

obj = Solution()
print(obj.floorSqrt(x))