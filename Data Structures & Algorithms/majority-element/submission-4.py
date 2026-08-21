class Solution: # boyer-moore algorithm, see neetcode solution
    def majorityElement(self, nums: List[int]) -> int:
        result: int = 0
        count: int = 0

        result = nums[0] # set to the first value
        for n in nums: 
            if n == result: 
                count += 1
            else:
                count -= 1

            # if count goes negative, then the current majority is replaced as it is no longer eligible
            if count < 0: 
                result = n
        
        return result
