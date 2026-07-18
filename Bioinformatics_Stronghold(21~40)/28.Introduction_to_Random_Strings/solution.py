import sys
import math

with open(sys.argv[1]) as f:
    DNA = f.readline().strip()
    GC_content_list = list(map(float, f.readline().strip().split()))

DNA_len = len(DNA)
n = len(GC_content_list)

def compute_random(a, n):
    if a == 'G' or a == 'C':
        return n/2
    elif a == 'A' or a == 'T':
        return (1-n)/2

for i in range(n):
    prob = 0 # common logarithm한 값을 더해주기 때문에 0으로 초기 설정
    for j in range(DNA_len):
        prob += math.log10(compute_random(DNA[j], GC_content_list[i]))
    print(f"{prob:0.3f}", end=' ')

print()
