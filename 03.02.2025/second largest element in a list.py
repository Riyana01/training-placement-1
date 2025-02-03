def second_largest(nums):
    if len(nums) < 2:
        return None 
    sorted_nums = sorted(nums, reverse=True)  
    return sorted_nums[1] 
numbers = [10, 30, 20, 40, 50]
result = second_largest(numbers)
if result is not None:
    print("Second largest element in the list:", result)
else:
    print("The list has less than two elements.")
