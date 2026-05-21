class Solution:
    def longestCommonPrefix(self, arr1, arr2):

        prefixes = set()

        for num in arr1:

            s = str(num)

            for i in range(1, len(s) + 1):

                prefixes.add(s[:i])

        answer = 0

        for num in arr2:

            s = str(num)

            for i in range(1, len(s) + 1):

                if s[:i] in prefixes:

                    answer = max(answer, i)

        return answer