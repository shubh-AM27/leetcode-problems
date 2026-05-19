class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        i = len(nums)
        if i % 2 == 1:
            return float(nums[i // 2])
        return (nums[i // 2 - 1] + nums[i // 2]) / 2.0