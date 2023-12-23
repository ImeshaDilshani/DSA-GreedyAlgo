def efficient_interval_cover(*xn):
    nums = list(xn)
    n = len(nums)

    nums.sort()
    intervals = []
    m = 0
    current_interval_start = nums[0]

    for i in range(1, n):
        num = nums[i]
        if num < current_interval_start + 1:
            continue
        else:
            intervals.append((current_interval_start, current_interval_start + 1))
            m += 1
            current_interval_start = num

    intervals.append((current_interval_start, current_interval_start + 1))
    m += 1

    return intervals, m


n = int(input("Enter the value of n (number of real numbers): "))
xn = []
for i in range(n):
    xn.append(float(input(f"Enter x{i + 1}: ")))

intervals, m = efficient_interval_cover(*xn)
print("Minimum number of unit intervals(m):", m)
print("Intervals:", intervals)
