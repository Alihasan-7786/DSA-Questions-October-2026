class Solution:
    def trimmedMean(self, scores, t):
        count = [0] * 101
        for score in scores:
            count[score] += 1
        remove = t
        for i in range(101):
            if remove == 0:
                break
            if count[i] <= remove:
                remove -= count[i]
                count[i] = 0
            else:
                count[i] -= remove
                remove = 0
        remove = t
        for i in range(100, -1, -1):
            if remove == 0:
                break
            if count[i] <= remove:
                remove -= count[i]
                count[i] = 0
            else:
                count[i] -= remove
                remove = 0
        total = 0
        remaining = 0
        for i in range(101):
            total += i * count[i]
            remaining += count[i]

        return total / remaining

n, t = map(int, input().split())
scores = list(map(int, input().split()))

obj = Solution()
answer = obj.trimmedMean(scores, t)

print("%.2f" % answer)