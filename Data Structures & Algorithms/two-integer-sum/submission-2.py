class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff= {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in diff:
                return [diff[complement], i]
            diff[n] = i