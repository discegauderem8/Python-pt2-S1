
nums = [1, 1, 2, 3, 3, 4, 5, 6, 6]

res = set(num for num in nums if nums.count(num) > 1)

print(*res)

