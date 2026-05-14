class Solution:
    def isGood(self, nums):

        nums.sort()

        n = nums[-1]

        expected = list(range(1, n)) + [n, n]

        return nums == expected