# Write a function that, given:
# 1. an amount of money
# 2. a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations

# Example: for `amount = 4` (4¢) and `denominations = [1,2,3]` (1¢, 2¢ and 3¢),
# your program would output 4 - the number of ways to make 4¢ with those denominations:
# 1. 1¢, 1¢, 1¢, 1¢
# 2. 1¢, 1¢, 2¢
# 3. 1¢, 3¢
# 4. 2¢, 2¢


def change_possibilities(denominations, amount):
    num_ways_to_make = [0 for _ in range(amount + 1)]
    num_ways_to_make[0] = 1

    for coin in denominations:
        for y in range(coin, amount + 1):
            num_ways_to_make[y] += num_ways_to_make[y - coin]

    return num_ways_to_make[amount]



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# First thought: DFS
# - For a given amount, go from largest denom possible, taking all possible number of that largest denom, subtracting it and resulting in a smaller amount
# - On that smaller amount, go from all but largest denoms possible, do the same thing
# - ... and so on
# Is there duplicate work? -> Yes
# - We are going top down which means we might be calculating multiple same denoms multiple times
# - e.g. denoms = {1, 2, 3}, amount = 100, we would be 94 with {1} twice (1 x 3, 0 x 2 and 0 x 3, 1 x 2)
# Also very difficult to keep track of which coins we have used
# Instead, can we go from bottom up?
# - Start from the number of possible ways to make 0 -> always 1
# - Then, to fix the problem of keeping track of which coins are used, we iterate on each coin instead
# - For each coin x, number of ways to make amount y should increase by number of ways to make amount (y - x). Iterate on this y from x to amount
# - Does it matter what order of coins we go in? No - all cases should be covered by the end anyway
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            change_possibilities([1, 2, 3], 4), 4
        )

if __name__ == '__main__':
    unittest.main()
