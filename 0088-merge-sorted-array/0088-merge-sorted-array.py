class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l= len(nums1)
        id=0

        for i in range(m,l):
            nums1[i]=nums2[id]
            id+=1

        nums1.sort()

        