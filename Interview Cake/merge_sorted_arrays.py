# Merge Sorted Arrays

# Example:
# list_1 = [3, 4, 6, 10, 11, 15]
# list_2 = [1, 5, 8, 12, 14, 19]
# result = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]


from typing import List


def merge_sorted_arrays(list_1: List[int], list_2: List[int]) -> List[int]:
    result = []
    index_1 = index_2 = 0

    while index_1 < len(list_1) and index_2 < len(list_2):
        if list_1[index_1] < list_2[index_2]:
            result.append(list_1[index_1])
            index_1 += 1
        else:
            result.append(list_2[index_2])
            index_2 += 1

    while index_1 < len(list_1):
        result.append(list_1[index_1])
        index_1 += 1
    while index_2 < len(list_2):
        result.append(list_2[index_2])
        index_2 += 1

    return result



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# To merge two sorted lists, use a pointer on each list. O(m + n) where m and n are lengths of each list respectively
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            merge_sorted_arrays([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]),
            [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
        )

if __name__ == '__main__':
    unittest.main()
