
class Solution:
    def firstDuplicate(self, arr):
        seen = set()
        for i in range(len(arr)):
            if arr[i] in seen:
                return arr[i]
            seen.add(arr[i])
        return -1

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.firstDuplicate(arr))