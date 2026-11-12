class Solution:
    def findMin(self, arr):
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo]

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.findMin(arr))