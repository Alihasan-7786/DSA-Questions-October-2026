class Solution:
    def containsNearbyDuplicate(self, arr, k):
        seen = {}
        for i in range(len(arr)):
            if arr[i] in seen:
                if i - seen[arr[i]] <= k:
                    return "YES"
            seen[arr[i]] = i
        return "NO"

n, k = map(int, input().split())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.containsNearbyDuplicate(arr, k))