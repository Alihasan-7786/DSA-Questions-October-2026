class Solution:
    def firstBadBuild(self, arr):
        lo = 0
        hi = len(arr) - 1
        answer = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == 1:
                answer = mid + 1
                hi = mid - 1
            else:
                lo = mid + 1
        return answer

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.firstBadBuild(arr))