from typing import List
import bisect

def lengthOfLIS(nums: List[int]) -> int:
    dp = []

    for num in nums:
        # Find the first element >= num
        pos = bisect.bisect_left(dp, num)

        if pos == len(dp):
            dp.append(num)
        else:
            dp[pos] = num

    return len(dp)


# Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]

print("Length of LIS:", lengthOfLIS(nums))
