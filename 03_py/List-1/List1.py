#Kyle Lee
#K^3 (Kyle, Suhana, Vedant)
#SoftDev
#K3 -- Python
#2024-09-15
#time spent: .75

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1];

def first_last6(nums):
  return nums[0] == 6 or nums[len(nums) - 1] == 6


def has23(nums):
  return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3


def make_ends(nums):
   new = [nums[0], nums[len(nums) - 1]]
   return(new)

def make_pi():
  x = [3, 1, 4];
  return x;


def max_end3(nums):
  a = 0;
  if (nums[0] > nums[len(nums) - 1]):
    a = nums[0];
  else:
    a = nums[len(nums) - 1];
  nums[0] = a;
  nums[1] = a;
  nums[2] = a;
  return nums;


def middle_way(a, b):
  new = [a[1], b[1]]
  return(new)


def reverse3(nums):
  nums_new = [nums[2], nums[1], nums[0]];
  return nums_new;


def rotate_left3(nums):
  nums_new = [nums[1], nums[2], nums[0]];
  return nums_new;

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[len(nums) - 1];

def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return nums[0]
  else:
    sum = nums[0] + nums[1]
    return(sum)


def sum3(nums):
  return nums[0] + nums[1] + nums[2];


