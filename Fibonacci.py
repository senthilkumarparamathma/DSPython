# 0,1,1,2,3,5,8,13,21

# time complexitey = O(2^n)
# space complexity = O(n)
def fibonacci(n):
  if n == 1:
    #print(0)
    return 0
  elif n == 2:
    #print(1)
    return 1
  else:
    previousn1 = fibonacci(n-1)
    previousn2 = fibonacci(n-2)
    res = previousn1 + previousn2
    return res

# time comeplexity = O(n)
# space complexity = O(n)
def fibonacciDP(n, cache = {1:0,2:1}):
  if n in cache:
    return cache[n]
  else:
    cache[n] = fibonacciDP(n-1,cache) + fibonacciDP(n-2,cache)
    return cache[n]

# time complexity = O(n)
# space complexity = O(1)
def fibonacciNoSpace(n):
  a = 0
  b =1
  if n == 1:
    return a
  elif n ==2:
    return b
  else:
    for i in range(2, n):
      c = a + b
      a = b
      b = c

  return c


print("@@---")
n = 10
for i in range(1,n +1):
  print("res = {0}".format(fibonacci(i)))
print("@@---")
for i in range(1,n +1):
  print("res dp = {0}".format(fibonacciDP(i)))

print("@@---")
for i in range(1,n +1):
  print("res no space = {0}".format(fibonacciNoSpace(i)))