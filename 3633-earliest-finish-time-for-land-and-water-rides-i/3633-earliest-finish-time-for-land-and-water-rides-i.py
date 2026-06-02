class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration
    ):

        def calc(start1, dur1, start2, dur2):

            min_end = min(s + d for s, d in zip(start1, dur1))

            ans = float('inf')

            for s, d in zip(start2, dur2):

                ans = min(ans, max(s, min_end) + d)

            return ans

        land_first = calc(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        water_first = calc(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return min(land_first, water_first)