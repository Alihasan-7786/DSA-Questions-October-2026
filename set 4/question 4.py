class Solution:
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)
        if m > n:
            return []
        text_count = [0] * 26
        pattern_count = [0] * 26
        for i in range(m):
            text_count[ord(s[i]) - ord('a')] += 1
            pattern_count[ord(p[i]) - ord('a')] += 1
        result = []
        if text_count == pattern_count:
            result.append(0)
        for i in range(m, n):
            text_count[ord(s[i]) - ord('a')] += 1
            text_count[ord(s[i - m]) - ord('a')] -= 1
            if text_count == pattern_count:
                result.append(i - m + 1)

        return result

s = input()
p = input()
obj = Solution()
result = obj.findAnagrams(s, p)

if result:
    print(*result)
else:
    print("None")