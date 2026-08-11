import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # [^a-zA-Z0-9] represents all non-alphanumeric characters, replace with second argument: '' (empty string), then lowercase the string
        bareString: str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        left: int = 0
        right: int = len(bareString) - 1

        while left < right:
            if bareString[left] != bareString[right]:
                return False
            else:
                left += 1
                right -= 1

        return True