"""
Function that calculates the fewest number of operations
"""

def minOperations(n):
  """
  Calculate fewest number of operations (copy all + paste) using n as the repetition count
  """

  if n < 2:
    return 0
  
  operations = 0
  factors = 2

  while factors <= n:
    if n % factors == 0:
      operations += factors
      n //= factors
    else:
      factors += 1
  return operations

print(minOperations(12))