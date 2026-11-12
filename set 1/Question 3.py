class Solution:
    def secondHighest(self, arr):
        first = None
        second = None
        for num in arr:
            if first is None or num > first:
                if num != first:
                    second = first
                    first = num
            elif num != first:
                if second is None or num > second:
                    second = num
        return second

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
result = obj.secondHighest(arr)

print(result if result is not None else "None")