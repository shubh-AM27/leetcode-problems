class Solution:
    def findThePrefixCommonArray(self, A, B):

        count = {}

        result = []

        common = 0

        for i in range(len(A)):

            count[A[i]] = count.get(A[i], 0) + 1

            if count[A[i]] == 2:
                common += 1

            count[B[i]] = count.get(B[i], 0) + 1

            if count[B[i]] == 2:
                common += 1

            result.append(common)

        return result