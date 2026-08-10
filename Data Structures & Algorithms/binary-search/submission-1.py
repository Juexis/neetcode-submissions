class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low: int = 0
        high: int = len(nums) - 1

        for i in range(len(nums)):
            mid: int = int((low + high) / 2)

            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                high = mid - 1
            
            elif target > nums[mid]:
                low = mid + 1
            
        return -1       
