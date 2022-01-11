from typing import List


def binary_search(nums: List[int], target: int) -> int:
    floor, ceil = 0, len(nums) - 1
    while floor <= ceil:
        mid = (floor + ceil) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            floor = mid + 1
        else:
            ceil = mid - 1
    return -1


def binary_search_v2(nums: List[int], target: int) -> int:
    floor, ceil = -1, len(nums)
    while floor + 1 < ceil:
        mid = (floor + ceil) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            floor = mid
        else:
            ceil = mid
