class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in res_dict:
                return [i, res_dict[target - nums[i]]]
            res_dict.update({nums[i]:i})