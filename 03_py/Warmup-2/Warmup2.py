#Kyle Lee
#K^3 (Kyle, Suhana, Vedant)
#SoftDev
#K3 -- Python
#2024-09-15
#time spent: .75

def string_times(str, n):
  string = ""
  for i in range(n):
    string += str
  return string

def front_times(str, n):
  string = ""
  autrestring = ""
  if len(str) <= 2:
    for i in range(n):
      string += str
    return string
  for i in range(3):
    autrestring += str[i]
  for i in range(n):
    string += autrestring
  return string

def string_bits(str):
  
  string = ""
  for i in range(len(str)):
    if (i%2 == 0):
      string += str[i]
  return string

def string_splosion(str):
  string = ""
  for i in range(len(str)+1):
    string = string + str[:i]
    
  return string

def last2(str):
  count = 0
  if (len(str) < 2):
    return count
  else:
    string = str[-2] + str[-1]
    for i in range(len(str)-2):
      if (string == str[i] + str[i+1]):
        count +=1
  return count

def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count +=1
  return count

def array_front9(nums):
  count = 0
  if (len(nums) < 4):
    for i in range(len(nums)):
      if nums[i] == 9:
        count +=1
  else:
    for i in range(4):
      if nums[i] == 9:
        count +=1
  return count > 0

def array123(nums):
  if (len(nums) < 2):
    return False
  else:
    for i in range(len(nums)-2):
      if (nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
        return True
  return False

def string_match(a, b):
  count = 0
  if len(a) < 2:
    return 0
  else :
    for i in range(min(len(a),len(b))-1):
      if (a[i] + a[i+1] == b[i] + b[i+1]):
        count +=1
    return count


