class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k: int = 0
        start: int = 0
        end: int = len(nums) - 1

        while start <= end:
            if nums[start] == val:
                # swap start and end
                cachedstart: int = nums[start]
                nums[start] = nums[end]
                nums[end] = cachedstart
                end -= 1 # allocate new space for a new swap 
                continue # go back to check if new start contains val

            # if nums[start] isn't val then we can move on to the next element
            start += 1
            k += 1

        return k
            



