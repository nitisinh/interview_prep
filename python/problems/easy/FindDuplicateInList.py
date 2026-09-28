"""
Given a list of numbers , find the duplicate number in the list
"""
def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    print(find_duplicate(nums))
    nums = [1, 2, 3, 4, 5, 6, 9, 8, 9, 1]
    print(find_duplicate(nums))
