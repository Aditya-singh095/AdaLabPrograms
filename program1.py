from typing import List

# 1. Search in Rotated Sorted Array
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# 2. Power Function - x^n
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0

    # Handle negative exponent
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0

    # Binary exponentiation
    while n > 0:
        if n % 2 == 1:
            result *= x

        x *= x
        n //= 2

    return result
