dna = input()

rna = dna[::-1]

for i in range(len(rna)):
    if rna[i] == 'A':
        rna[i] = 'T'
    elif rna[i] == 'T':
        rna[i] = 'A'
    elif rna[i] == 'C':
        rna[i] = 'G'
    elif rna[i] == 'C':
        rna[i] = 'G'

print(rna)



# dna = input()

# # 상보 염기쌍 딕셔너리
# complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# # 1. 역순으로 뒤집고 2. 각 염기를 상보 염기로 변환
# rna = "".join([complement[base] for base in dna[::-1]])

# print(rna)