class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        the simplest way of tansversing all the list elements and search for the two wanted.
        O(n^2）
        '''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []
