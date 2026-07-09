n = int(input())

basket = []
for i in range(1, n+1):
    basket.append(i)

# 가짓수 출력하기
answer = 1
for i in range(1, n+1):
    answer *= i
print(answer)

# 재귀함수를 활용한 permutation 함수 -> itertools의 permutation 함수도 있음
def permutations(current, remaining):
    if not remaining:
        print(' '.join(str(i) for i in current))
        return
    for i in range(len(remaining)):
        next_current = current + [remaining[i]]
        next_remaining = remaining[:i] + remaining[i+1:]
        permutations(next_current, next_remaining)

permutations([], basket)