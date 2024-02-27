from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       test_dict = {}
       for i in range(len(nums)):
           test_dict[target-nums[i]] = i
       for i in range(len(nums)):
           if nums[i] in test_dict and test_dict[nums[i]]!=i:
               return(i,test_dict[nums[i]])
 
# Main172913
nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))