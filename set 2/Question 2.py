class Solution:
    def firstUnique(self, arr):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num in arr:
            if freq[num] == 1:
                return num
        return -1

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.firstUnique(arr))
