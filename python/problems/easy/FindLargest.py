"""
Given a list of numbers, find the largest number in the list
"""
def find_largest(nums):
    if not nums:
        return None
    largest = nums[0]
    for num in nums[1:]:
        if num > largest:
            largest = num
    return largest

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    print(find_largest(nums))
    nums = [1, 2, 3, 4, 5, 6, 9, 8, 9, 1]
    print(find_largest(nums))   