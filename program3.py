from typing import List, Tuple

def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k - 1]


def findMinMax(nums: List[int]) -> Tuple[int, int]:
    return min(nums), max(nums)


# Example
nums = [3, 1, 5, 2, 4]

print("Kth largest:", findKthLargest(nums, 2))
print("Min and Max:", findMinMax(nums))
