class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        sums = []
        for i in range(0,len(nums)):
            complement = target - nums[i]
            
            if complement in dictionary:
                sums.append(nums.index(complement))
                sums.append(i)
                
                
            
            dictionary[nums[i]] = nums[i]
        return sums
