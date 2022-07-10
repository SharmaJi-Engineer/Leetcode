# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# The following solution when ran resulted in "Time Limit Exceeded"
# Time:O(n^2)   Space: O(1)
def containsNearbyDuplicate_naive(nums, k):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j] and abs(i-j)<=k:
                return True
    return False

# The following solution was accepted
# Time:O(n)   Space: O(n)
def containsNearbyDuplicate_hashMap(nums, k):
    seen = dict()
    for index,val in enumerate(nums):
        if val in seen:
            if abs(seen[val] - index) <=k:
                return True
        seen[val] = index
    return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    print(f"duplicate with index found in {nums} : {containsNearbyDuplicate_hashMap(nums,k)}")
    nums = [1,0,1,1]
    k = 1
    print(f"duplicate found in {nums} : {containsNearbyDuplicate_hashMap(nums,k)}")
    nums = [1,2,3,1,2,3]
    k = 2
    print(f"duplicate found in {nums} : {containsNearbyDuplicate_hashMap(nums,k)}")
