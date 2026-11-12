class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0
        for num in arr:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.majorityElement(arr))