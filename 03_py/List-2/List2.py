#Kyle Lee
#K^3 (Kyle, Suhana, Vedant)
#SoftDev
#K3 -- Python
#2024-09-15
#time spent: .75

def count_evens(nums):
  counter = 0
  for item in nums:
    if (item % 2) == 0:
      counter += 1
  return counter

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  Sum = 0
  for item in nums:
    Sum += item
  return (Sum-max(nums)-min(nums))/(len(nums)-2)

def sum13(nums):
  Sum = 0
  i = 0
  while i < (len(nums)):
    if nums[i]==13:
      i += 2
    else:
      Sum += nums[i]
      i += 1
  return Sum

def sum67(nums):
  total = 0
  skip = False
  for num in nums:
    if num == 6:
      skip = True
    elif skip:
      if num == 7:
        skip = False
    else: 
      total += num
  return total

def has22(nums):
  for i in range (len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False
