import sys

# 단백질이 있을 때 가능한 codon의 수
codon_counts = {
    'F': 2, 'L': 6, 'I': 3, 'M': 1, 'V': 4,
    'S': 6, 'P': 4, 'A': 4, 'Y': 2, 'H': 2,
    'Q': 2, 'T': 4, 'N': 2, 'K': 2, 'D': 2,
    'E': 2, 'C': 2, 'W': 1, 'R': 6, 'G': 4
}

with open(sys.argv[1]) as f:
    protein = f.read().strip()

output = 1

# modulo 1000000를 계속 처리하면서 곱하기 
for i in range(len(protein)):
    a = codon_counts[protein[i]] % 1000000
    output *= a
    output = output%1000000

# 마지막까지 modulo 처리
print(output*3%1000000) # stop codon 고려 (가지수 3개)