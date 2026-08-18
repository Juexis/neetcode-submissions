class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercases: str = s.lower()

        left: int = 0
        right: int = len(lowercases) - 1

        while left < right:
            if not lowercases[left].isalnum():
                left += 1
                continue

            if not lowercases[right].isalnum():
                right -= 1
                continue

            if lowercases[left] != lowercases[right]:
                return False
                
            else:
                left += 1
                right -= 1
                
        return True
    