class Solution:
    def popularitySort(self, arr):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        unique = list(freq.keys())
        for i in range(len(unique) - 1):
            for j in range(i + 1, len(unique)):
                a = unique[i]
                b = unique[j]
                if freq[a] > freq[b] or (freq[a] == freq[b] and a < b):
                    unique[i], unique[j] = unique[j], unique[i]

        result = []
        for num in unique:
            for i in range(freq[num]):
                result.append(num)
        return result

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(*obj.popularitySort(arr))