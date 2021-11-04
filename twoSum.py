class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_x = {}
        lens = len(nums)
        count = 0
        while count<lens:
            val = target - nums[count]
            if (val in dict_x):
                return[dict_x[val],count]
            dict_x[nums[count]] = count
            count+=1
