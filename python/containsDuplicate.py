# Leetcode problem - 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# The following 2 solutions when ran resulted in "Time Limit Exceeded"
# Time:O(n^2)   Space: O(1)
def containsDuplicate_Naive(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]== nums[j]: return True
    return False
                

# Time:O(n^2)   Space: O(n)
def containsDuplicate_List(nums):
    # create empty list
    seen = list()
    for num in nums:
        # if this num is already seen before, then num is duplicate
        if num in seen:
            return True
        # num is not seen before, add it to the list
        seen.append(num)
    # all nums are distinct    
    return False
                

# The following 2 solutions were "Accepted"
# Time:O(nlogn)   Space: O(1)
def containsDuplicate_sort(nums):               
    nums.sort()
    for i in range(1,len(nums)):
        # return true when neighbours have same value 
        if nums[i] == nums[i-1]: return True
    return False
                    
# Time:O(n)   Space: O(n)
def containsDuplicate_set(nums):
    # create empty set
    seen = set()
    for num in nums:
        # if this num is already seen before, then num is duplicate
        if num in seen:
            return True
        # num is not seen before, add it to the set
        seen.add(num)
    # all nums are distinct
    return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(f"duplicate found in {nums} : {containsDuplicate_set(nums)}")
    nums = [1,2,3,4]
    print(f"duplicate found in {nums} is: {containsDuplicate_set(nums)}")
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(f"duplicate found in {nums} is: {containsDuplicate_set(nums)}")
