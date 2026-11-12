class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return "NO"
            else:
                left += 1
                right -= 1

        return "YES"


s = input()

obj = Solution()
print(obj.isPalindrome(s))