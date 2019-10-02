# Given an array of integers, return indices of the two numbers such that they add up to a specific target
# You may assume that each input would have exactly one solution, and you may not use the same element twice

nums = [12, 17, 1, 14]
target = 26

for i, n in enumerate(nums):
    check = target - n
    if check in nums:
        i2 = nums.index(check)
        print(f'nums [{i}] + nums[{i2}] = {nums[i]} + {nums[i2]} = {target}')
        break
