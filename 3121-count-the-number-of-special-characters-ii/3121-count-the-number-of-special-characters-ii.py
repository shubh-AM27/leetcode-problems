class Solution:
    def numberOfSpecialChars(self, word):

        last_lower = {}
        first_upper = {}

        for i, ch in enumerate(word):

            if ch.islower():

                last_lower[ch] = i

            else:

                lower = ch.lower()

                if lower not in first_upper:
                    first_upper[lower] = i

        answer = 0

        for ch in last_lower:

            if ch in first_upper:

                if last_lower[ch] < first_upper[ch]:

                    answer += 1

        return answer