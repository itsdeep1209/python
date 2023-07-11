# Given an array of two integers nums and an integer target , return indices of the two numbers such that they add up to target

def two_sum(nums,target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return[i,j]
    return[]

nums = [2,7,11,15]
target = 9
s = two_sum(nums,target)
print("sum is", s)