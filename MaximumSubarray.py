class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final = nums[0]
        current_max = 0
        for i in range(len(nums)):
            if current_max < 0:
                current_max = 0
            current_max += nums[i]
            final = max(final, current_max)
        return final