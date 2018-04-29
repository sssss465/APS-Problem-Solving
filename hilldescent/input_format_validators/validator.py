# This is a python3 validator

import sys, re

n_line = sys.stdin.readline()

if re.match('^[1-9]\d*\s[1-9]\d*$', n_line) == None:
  sys.exit(1) # invalid n
n_line = n_line.split(' ')
n = int(n_line[0])
m = int(n_line[1])

if (n < 0 or m < 0 or m > 1000 or n > 1000):
  sys.exit(2) # invalid m or n value.




for i in range(n):
  line = sys.stdin.readline().split(" ")
  if len(line) != m:
    sys.exit(3) #invalid line length
  for j in range(m):
    if re.match('^0\s|^[1-9]\d*', line[j]) == None:
        sys.exit(4) #invalid input format for a single int.
    if int(line[j]) > 1000000 or int(line[j]) < 0:
      sys.exit(5) # invalid range for a[i][j]

line = sys.stdin.readline()
if len(line) > 0:
  sys.exit(7) # last line is not empty

# an input validator must exit with code 42 to for success
sys.exit(42)
