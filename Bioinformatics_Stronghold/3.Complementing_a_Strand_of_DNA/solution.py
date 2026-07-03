import sys

# dna input 받고 좌우반전
dna = open(sys.argv[1]).read().strip()
dna = dna[::-1]
rna = []

# complement 표를 생성 후에 이를 for문으로 적용
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

for i in range(len(dna)):
    rna.append(complement[dna[i]])

print(''.join(rna))  