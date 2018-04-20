# This is a python2 validator

import sys, re

n_line = sys.stdin.readline()

if re.match('^[1-9]\d*$', n_line) == None:
  sys.exit(1) # invalid n

n = int(n_line)

nums_line = sys.stdin.readline()
# Here we match n integers. An integer must not have leading zero.
if re.match('^(0|-?[1-9]\d*)( (0|-?[1-9]\d*)){%d,%d}$' % (n-1, n-1), nums_line) == None:
  sys.exit(2) # invalid numbers

nums = [int(x) for x in nums_line.split(' ')]

if max(nums) > 100 or min(nums) < -100:
  sys.exit(3) # numbers out of range

# an input validator must exit with code 42 to for success
sys.exit(42)
