import sys
import math

with open(sys.argv[1]) as f:
    dna = ''.join(f.read().split('\n')[1:])

num_A = dna.count('A')
num_C = dna.count('C')

print(math.factorial(num_A) * math.factorial(num_C))