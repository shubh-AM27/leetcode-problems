from functools import lru_cache

class Solution:

    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x):

            if x < 0:
                return 0

            s = str(x)

            @lru_cache(None)
            def dp(pos, prev2, prev1, tight, started):

                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                ways = 0
                waviness = 0

                for d in range(limit + 1):

                    ntight = tight and d == limit

                    if not started and d == 0:

                        cnt, wav = dp(
                            pos + 1,
                            -1,
                            -1,
                            ntight,
                            False
                        )

                        ways += cnt
                        waviness += wav

                    else:

                        extra = 0

                        if prev2 != -1:

                            if (
                                prev1 > prev2 and prev1 > d
                            ) or (
                                prev1 < prev2 and prev1 < d
                            ):
                                extra = 1

                        cnt, wav = dp(
                            pos + 1,
                            prev1,
                            d,
                            ntight,
                            True
                        )

                        ways += cnt
                        waviness += wav + extra * cnt

                return ways, waviness

            return dp(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)