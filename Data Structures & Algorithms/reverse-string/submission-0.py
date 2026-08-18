class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        left: int = 0
        right: int = len(s) - 1

        while left < right:
            temp: str = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1

        """
        Do not return anything, modify s in-place instead.
        """
        