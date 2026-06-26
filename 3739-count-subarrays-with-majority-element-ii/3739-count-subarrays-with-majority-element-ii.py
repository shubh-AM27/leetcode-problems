class BinaryIndexedTree:

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):

        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):

        ans = 0

        while i > 0:
            ans += self.tree[i]
            i -= i & -i

        return ans


class Solution:
    def countMajoritySubarrays(self, nums, target):

        n = len(nums)

        bit = BinaryIndexedTree(2 * n + 1)

        prefix = n + 1

        bit.update(prefix, 1)

        ans = 0

        for x in nums:

            if x == target:
                prefix += 1
            else:
                prefix -= 1

            ans += bit.query(prefix - 1)

            bit.update(prefix, 1)

        return ans    