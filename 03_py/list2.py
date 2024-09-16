def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count

def big_diff(nums):
  maxNum = nums[0]
  minNum = nums[0]
  for i in range(len(nums)):
    maxNum = max(maxNum, nums[i])
    minNum = min(minNum, nums[i])
  return maxNum - minNum

def centered_average(nums):
  maxNum = nums[0]
  minNum = nums[0]
  for i in range(len(nums)):
    maxNum = max(maxNum, nums[i])
    minNum = min(minNum, nums[i])
  
  sums = 0
  for num in nums:
    sums += num
  return (sums - (maxNum + minNum)) / (len(nums) - 2)

def sum13(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 13:
      continue
    if nums[i-1] == 13 and not i == 0:
      continue
    count += nums[i]
  return count

def sum67(nums):
  sums = 0
  six = True
  for num in nums:
    if num == 6:
      six = False
    if six:
      sums += num
    if num == 7:
      six = True
  return sums

def has22(nums):
  for i in range(len(nums) - 1):
    if (nums[i] == 2 and nums[i+1] == 2):
      return True
  return False
