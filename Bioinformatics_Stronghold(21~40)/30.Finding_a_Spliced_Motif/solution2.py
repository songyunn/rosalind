import sys

with open(sys.argv[1]) as f:
    data = f.read().strip().split('>')
    DNA = ''.join(data[1].split('\n')[1:])
    motif = ''.join(data[2].split('\n')[1:])

indexes = []
# print(motif, DNA)
# 시간 복잡도를 DNA 길이로 줄임
for i in range(len(DNA)):
    a = len(indexes)
    if a == len(motif):
        break
    elif motif[a] == DNA[i]:
        indexes.append(i+1)


print(' '.join(map(str, indexes)))
# >Rosalind_14
# ACGTACGTGACG
# >Rosalind_18
# GTA