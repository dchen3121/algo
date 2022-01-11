# You are cake thief.
# Each type of cake has a weight and a value, stored in a tuple with two indices:
# - An integer representing the weight of the cake in kilograms
# - An integer representing the monetary value of the cake in British shillings

# For Example:
# A cake that weighs 7 kilograms and has a value of 160 shillings: (7, 160)
# A cake that weighs 3 kilograms and has a value of 90 shillings: (3, 90)

# Write a function that takes a list of cake type tuples and a weight capacity,
# and returns the maximum monetary value the duffel bag can hold.

from typing import Tuple


# old top-down version
def unbounded_knapsack_rec(cakes: Tuple[int, int], weight_limit: int) -> int:
    min_cake_val = min(cake[0] for cake in cakes)

    def rec_help(weight_limit, profit):
        if weight_limit < min_cake_val:
            return profit
        max_profit = profit
        for cake in cakes:
            weight, value = cake
            if weight_limit >= weight:
                max_profit = max(max_profit, rec_help(weight_limit - weight, profit + value))
        return max_profit

    return rec_help(weight_limit, 0)


def unbounded_knapsack(cakes: Tuple[int, int], weight_limit: int):
    max_values_at_weight = [0 for _ in range(weight_limit + 1)]

    for weight_lim in range(weight_limit + 1):
        for cake in cakes:
            weight, value = cake
            if weight <= weight_lim:
                max_values_at_weight[weight_lim] = max(max_values_at_weight[weight_lim], max_values_at_weight[weight_lim - weight] + value)

    return max_values_at_weight[weight_limit]

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# First thought: can we be greedy here and pick the cakes with the best average values first?
# - No -> think of cake that cost 3 and cake that costs 7
# Second thought: can we use DFS?
# - Start from weight limit, use one cake, we get new weight limit and value, keep recursing, pick best one
# - Might be too much duplicate work - the same weight limit might get visited multiple times
# Third thought: can we memoize?
# - Start from weight 0 - max profit here is 0
# - For each weight greater than 0, iterate through each cake
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            unbounded_knapsack_rec([(3, 50), (7, 110), (9, 155)], 10), 160
        )

if __name__ == '__main__':
    unittest.main()
