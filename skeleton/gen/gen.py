# This is an example generator that generates n random integers.
# You may write a wrapper script that calls random_case with different arguments,
# and directs its output to multiple .in files.

import random

MAX_VAL = 100

def random_case(n):
  res = '%d\n' % n
  res += ''.join([random.randint(-MAX_VAL, MAX_VAL) for _ in range(n)]) + '\n'
  return res
  
print random_case(5)