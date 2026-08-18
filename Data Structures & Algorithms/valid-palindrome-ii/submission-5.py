class Solution:
    # helper function to check if sliced version would be a palindrome
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        # using two pointers to save space instead of slicing, i and j serve the same purpose as left and right
        i: int = left
        j: int = right
            
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1

        while left < right:

            # check mismatch
            if s[left] != s[right]:
                # use helper function to check if next letters in line allow it to be palindrome
                if self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1):
                    return True
                # if mismatch and next letters don't make it a palindrome, then it must be false
                else:
                    return False

            left += 1
            right -= 1
        return True




