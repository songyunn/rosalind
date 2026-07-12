alphabet = input().split(' ')
a = int(input())
result = []

# 재귀함수를 활용한 permutation 함수 -> itertools의 permutation 함수도 있음
# 19번 함수 재사용 -> 원하는 길이 되면 바로 끝나고 출력하는 걸로 변경
def permutations(current, remaining, a, result):
    if len(current) == a:
        result.append(''.join(str(i) for i in current))
        return
    for i in range(len(remaining)):
        next_current = current + [remaining[i]]
        permutations(next_current, remaining, a, result)

permutations([], alphabet, a, result)
result = sorted(result)

for i in result:
    print(i)