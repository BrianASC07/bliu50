def string_times(str, n):
  return n * str

def front_times(str, n):
  return n * str[:3]

def string_bits(str):
  string = str[0::2]
  return string

def string_splosion(str):
  output = ''
  for i in range (len(str)):
    output += str[:i + 1]
  return output

def last2(str):
  if len(str) < 2:
    return 0
  
  substring = str[len(str) -2:]
  count = 0
  for i in range(len(str) - 2):
    sub = str[i:i+2]
    if sub==substring:
      count += 1
  return count

def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count += 1
  return count

def array_front9(nums):
  count = 0
  if len(nums) > 4:
    for num in range(0,4):
      if nums[num] == 9:
        return True
  else:
    for num in nums:
      if num == 9:
        return True
  return False

def array123(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 1 and i < len(nums) - 2:
      if nums[i + 1] == 2:
        if nums[i + 2] == 3:
          return True
  return False

def string_match(a, b):
  count = 0
  for i in range(len(a)-1):
    if a[i:i+2]==b[i:i+2]:
      count += 1
      
  return count
