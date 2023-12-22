def efficient_interval_cover(nums):
    nums.sort()
    intervals = []
    
    current_interval_start = nums[0]

    for num in nums[1:]:
        if num < current_interval_start + 1:
            continue
        else:
            intervals.append((current_interval_start, current_interval_start + 1))
            current_interval_start = num
    
    intervals.append((current_interval_start, current_interval_start + 1)) 
    return intervals

userInput = input("Enter real numbers separated by spaces: ")
inputNumbers = [float(x) for x in userInput.split()]

# input_numbers = [0.1, 0.9, 1.1, 1.555]
intervals = efficient_interval_cover(inputNumbers)
print("Minimum number of intervals:", len(intervals))
print("Intervals:", intervals)
