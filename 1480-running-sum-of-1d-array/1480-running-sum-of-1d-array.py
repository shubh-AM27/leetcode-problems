class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        sum = 0
        for i in range (n):
            sum = sum + nums[i]
            nums[i] = sum
        return nums