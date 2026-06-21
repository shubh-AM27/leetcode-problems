class Solution:
    def maxIceCream(self, costs, coins):

        freq = [0] * 100001

        for c in costs:
            freq[c] += 1

        ans = 0

        for cost in range(1, 100001):

            if freq[cost] == 0:
                continue

            can_buy = min(freq[cost], coins // cost)

            ans += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return ans