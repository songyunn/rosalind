import sys

# GC content 계산 함수
def computing_GC(strand):
    C = strand.count('C')
    G = strand.count('G')
    return (C+G)/len(strand)

# 한줄 씩 리스트로 받기
with open(sys.argv[1]) as f:
    dataset = [line.strip() for line in f.readlines()]

# max 변수 선언
max_GC = 0
max_lable = ''

# dataset list를 for loop으로 돌면서 DNA 시작 부분 찾기
# DNA 시작 부분 찾은 후에는 GC content 계산 -> max 값 비교 후 대입
for i in range(len(dataset)):
    if dataset[i][0] == '>':
        DNA = []
        a = i+1
        while dataset[a][0] != '>':
            DNA.append(dataset[a])
            a += 1
            # out of range 오류 해결하기
            if a >= len(dataset):
                break

        # 구한 GC와 MAX_GC 비교해서 하나만 저장하기
        compute_GC = computing_GC(''.join(DNA).strip()) 
        if max_GC < compute_GC:
            max_GC = compute_GC
            max_lable = dataset[i]

print(max_lable[1:])
print(max_GC*100)
    
# DNA list를 초기화 시키 않아서 한번 틀림