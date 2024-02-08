from typing import List


def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[List[int]]:
    nums_bounded = [lower - 1] + nums + [upper + 1]

    nums_bounded = [
        nums_bounded[i]
        for i in range(len(nums_bounded))
        if (nums_bounded[i] >= lower - 1 and nums_bounded[i] <= upper + 1)
    ]

    diffs = [
        nums_bounded[i + 1] - nums_bounded[i] for i in range(len(nums_bounded) - 1)
    ]

    result = []
    for i in range(len(nums_bounded) - 1):
        if diffs[i] > 1:
            result.append([nums_bounded[i] + 1, nums_bounded[i + 1] - 1])
    return result


nums = [1, 4]
lower = 0
upper = 3

findMissingRanges(nums, lower, upper)
