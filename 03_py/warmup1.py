def sleep_in(weekday, vacation):
  return ((not weekday) or (vacation))

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  if (a ==b):
    return 2 * (a+b)
  return a + b

def diff21(n):
  if n > 21:
    return 2 * abs(n-21)
  return abs(n-21)

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return (a==10 or b==10 or a + b ==10)

def near_hundred(n):
  return (abs(n-100)<=10 or abs(n-200)<=10)

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  return (a > 0 and b < 0) or (a < 0 and b > 0)

def not_string(str):
  if str[:3] == "not":
    return str
  return "not " + str

def missing_char(str, n):
  half = str[:n]
  secondhalf = str[n + 1: len(str)]
  return half + secondhalf

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  
  
  return str[len(str)-1] + mid + str[0]

def front3(str):
  return 3 * str[:3]
