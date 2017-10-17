# Uses python3\n",
# There are two ways of running this program:\n",
# 1. Run\n",
#     python3 APlusB.py\n",
# then enter two numbers and press ctrl-d/ctrl-z\n",
# 2. Save two numbers to a file -- say, dataset.txt.\n",
# Then run\n",
#     python3 APlusB.py < dataset.txt\n",

import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
