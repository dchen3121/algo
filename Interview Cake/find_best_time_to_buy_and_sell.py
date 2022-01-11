# Find Best Time to Buy and Sell
# Input is a list of integers, containing the different stock prices in a day.
# No shorting - you must buy before you sell

# Example:
# input: [10, 7, 5, 8, 11, 9]
# output: 6  (11 - 5)


from typing import List


def get_max_profit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0

    max_profit = prices[1] - prices[0]
    min_price = min(prices[0], prices[1])
    for i in range(2, len(prices)):
        max_profit = max(prices[i] - min_price, max_profit)
        min_price = min(prices[i], min_price)

    return max_profit



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Greedy approach - keep track of best profit + min price so far. O(n) where n is length of prices list
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            get_max_profit([10, 7, 5, 8, 11, 9]), 6
        )

if __name__ == '__main__':
    unittest.main()
