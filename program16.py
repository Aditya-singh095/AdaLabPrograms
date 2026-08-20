from typing import Iterator, Optional
import random


# --------------------------------
# KMP String Matching
# --------------------------------

def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    # Build LPS (Longest Prefix Suffix) array
    lps = [0] * len(needle)

    length = 0
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search needle inside haystack
    i = 0
    j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == len(needle):
                return i - j

        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


# --------------------------------
# Reservoir Sampling
# --------------------------------

class Randomizer:

    def __init__(self, stream):
        self.stream = stream
        self.selected = None

    def getRandom(self) -> int:
        """
        Return one uniformly random element from the stream.
        """

        selected = None

        for i, value in enumerate(self.stream, start=1):

            # Replace selected element with probability 1/i
            if random.randint(1, i) == 1:
                selected = value

        return selected


# --------------------------------
# Examples
# --------------------------------

print("KMP result:")
print(strStr("hello", "ll"))

print("\nRandom stream sample:")

stream = [10, 20, 30, 40, 50]

randomizer = Randomizer(stream)

print(randomizer.getRandom())
