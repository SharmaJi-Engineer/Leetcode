# 442. Find All Duplicates in an Array
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice,
# return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

# Example 2:
# Input: nums = [1]
# Output: []

# Time:O(n)   Space: O(n)
def findAllDuplicates(nums):
    seen = set()
    duplicate = set()
    for val in nums:
        # add value to set if seen and was not added to the result
        if val in seen and val not in duplicate:
            duplicate.add(val)
        else:
            seen.add(val)
    # covert set to list
    return(list(duplicate))

# idea: negation trick
# since the array is of size n and the values are in the range 1...n, each value can be seen as an index in the array.
# 1.e  (value at array) - 1 --> index in the array. Negate the value[index] if it is non-negative, otherwise the index is a duplicate.
# Time:O(n)   Space: O(1)
def findAllDuplicates_NegationTrick(nums):
    duplicate = list()
    for i in range(len(nums)):
        # represent value as an index by subtracting 1
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            # if the value at index is -ve, then index+1 is duplicate
            duplicate.append(index + 1)
        else:
            # set the value at index to -ve
            nums[index] = -nums[index]
    return duplicate
                

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(f"duplicate in {nums} are : {findAllDuplicates_NegationTrick(nums)}")
    nums = [1,1,2]
    print(f"duplicate in {nums} are : {findAllDuplicates_NegationTrick(nums)}")
    nums = [1]
    print(f"duplicate in {nums} are : {findAllDuplicates_NegationTrick(nums)}")
