import sys

with open(sys.argv[1]) as f:
    data = f.read().strip().split('>')
    DNA = ''.join(data[1].split('\n')[1:])
    motif = ''.join(data[2].split('\n')[1:])

indexes = []
# 시간 복잡도가 mofit * DNA인데 DNA 길이로 복잡도를 줄이는것이 좋다 
for i in motif:
    # base가 동일한 index다 모으기
    result = [e for e in range(len(DNA)) if DNA[e] == i] 
    # 그전 index보다 더 숫자가 높으면 삽입
    for j in result:
        if len(indexes) == 0:
            indexes.append(j+1)
            break
        elif j > indexes[-1]-1:
            indexes.append(j+1)
            break

print(' '.join(map(str, indexes)))
# >Rosalind_14
# ACGTACGTGACG
# >Rosalind_18
# GTA