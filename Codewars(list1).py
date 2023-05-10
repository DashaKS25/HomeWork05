#https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
def invert(lst):
  result = []
  for num in lst:
    num *= -1
    result.append(num)
  print(result)
  return result