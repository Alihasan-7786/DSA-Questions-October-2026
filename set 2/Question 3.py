class Solution:
    def longestStreak(self, arr, T):
        count = 0
        longest = 0
        for num in arr:
            if num >= T:
                count += 1
                if count > longest:
                    longest = count
            else:
                count = 0
        return longest

n, T = map(int, input().split())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.longestStreak(arr, T))