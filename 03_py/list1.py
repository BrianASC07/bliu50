def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  return False

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  return False

def make_pi():
  pi = [3, 1, 4]
  return pi

def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  return False

def sum3(nums):
  counter = 0
  sum = 0
  while counter < len(nums):
    sum += nums[counter]
    counter += 1
  return sum

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(nums):
  if nums[0] > nums[2]:
    return [nums[0], nums[0], nums[0]]
  return [nums[2], nums[2], nums[2]]

def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return nums[0]
  return nums[0] + nums[1]

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
    return True
  return False
