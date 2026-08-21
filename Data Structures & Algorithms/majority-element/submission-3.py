class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result: int = 0
        count: int = 0

        result = nums[0]
        for n in nums: 
            if n == result:
                count += 1
            else:
                count -= 1

            if count < 0:
                result = n
        
        return result
