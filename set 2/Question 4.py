class Solution:
    def rangeSum(self, arr, queries):
        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] + arr[i]
        result = []
        for l, r in queries:
            result.append(prefix[r + 1] - prefix[l])
        return result

n, q = map(int, input().split())
arr = list(map(int, input().split()))

queries = []
for i in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

obj = Solution()
result = obj.rangeSum(arr, queries)

for ans in result:
    print(ans)