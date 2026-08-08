class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        answer: List[int] = []
        dictNums = {}
        
        for i in range(len(nums)): # i refers to the actual number, not the index
            difference: int = target - nums[i]
            print(difference)

            if difference in dictNums.keys():
                answer = [dictNums[difference], i]
            else:
                dictNums.update({nums[i]: i})

        print(dictNums)
        return answer