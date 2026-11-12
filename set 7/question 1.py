class Solution:
    def search(self, arr, q):
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == q:
                return mid
            elif arr[mid] < q:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

obj = Solution()
print(obj.search(arr, q))