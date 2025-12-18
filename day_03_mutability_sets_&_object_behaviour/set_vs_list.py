nums_list = list(range(1_000_000))
nums_set = set(nums_list)

# List search (slow)
print(999999 in nums_list)

# Set search (fast)
print(999999 in nums_set)
