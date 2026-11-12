class Solution:
    def longestUniqueRun(self, arr):
        seen = {}
        left = 0
        longest = 0
        for right in range(len(arr)):
            if arr[right] in seen and seen[arr[right]] >= left:
                left = seen[arr[right]] + 1
            seen[arr[right]] = right
            length = right - left + 1
            if length > longest:
                longest = length

        return longest

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.longestUniqueRun(arr))