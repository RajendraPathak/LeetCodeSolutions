def twoSum(self, nums: List[int], target: int) -> List[int]:
    d1 = {}
    for index, value in enumerate(nums):
        if target - nums[index] in d1:
            return d1[target - nums[index]], index
        d1[value] = index