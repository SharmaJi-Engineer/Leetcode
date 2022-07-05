# Leetcode problem - 287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# The idea here is that since the array length is n+1 and the range of the values is [1,n]
# 1. There will be atleast one duplicate (since we have to fill N+1 positions with N numbers)
# 2. If we look at the values in the list as an index, there will be one index to which multiple
#    values will be pointing to, in the case below, both the values at index 3,4 are pointing to
#    index 2. This is similar to a cycle in linked list and can be solved using Floyd's Algorithm.
# Example:
#                0 1 2 3 4 <-- index
# Input: nums = [1,3,4,2,2]
#                0 --> 3 --> 2 --> 4 
#                            |<--- |

# Time:O(n)   Space: O(1)
def findDuplicate(nums):
    # 2 pointers starting from the index 0 
    slow = 0
    fast = 0
    while True:
        # move slow pointer forward by 1 position, fast by 2
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break;  # fast and slow pointers met
            
    slow2 = 0  # create another pointer starting at index 0
    while True:
        # move both the slow pointers forward by 1 position
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            # slow pointers met, this is the starting of the cycle,
            # return slow pointer which is the duplicate value
            return slow


if __name__ == "__main__":
    nums = [1,3,4,2,2]
    print(f"duplicate in {nums} is: {findDuplicate(nums)}")
    nums = [3,1,3,4,2]
    print(f"duplicate in {nums} is: {findDuplicate(nums)}")
