## We have a sorted list of numbers 'nums'. 
## Need to remove the duplicates in-place such that each unique element appears only once.
## The relative order of the elements should be kept the same.


### Answer:
# This is a sorted array. So, duplicate numbers will be present nearby.
# So, we can use two pointers to solve this. If 2 adjacent numbers are not the same,
# we can increment the first pointer and update it's value with the value of 2nd pointer.

## Time - O(n) - sorted array, i & j traverses n steps
## Space - O(1)

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]
    return i+1

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = removeDuplicates(nums)
    print(' '.join(map(str, nums[:res])))

