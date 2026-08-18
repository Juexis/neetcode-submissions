class Solution:
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        small_s: str = s[left:right]
            
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                # check if the next letter in line is equal, allowing the current letter to be "deleted"
                if self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1):
                    return True
                else:
                    return False

            left += 1
            right -= 1
        return True




