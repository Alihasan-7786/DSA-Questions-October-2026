class Solution:
    def searchRange(self, arr, x):
        first = -1
        last = -1
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] >= x:
                hi = mid - 1
            else:
                lo = mid + 1
            if arr[mid] == x:
                first = mid
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] <= x:
                lo = mid + 1
            else:
                hi = mid - 1
            if arr[mid] == x:
                last = mid

        return first, last

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

obj = Solution()
first, last = obj.searchRange(arr, x)
print(first, last)