import math

# combination 함수
def combination(a, b):
    output = 1
    for i in range(b):
        output *= a-i
    output /= math.factorial(b)
    return(output)

k, N = map(int, input().split())

n = 2**k # k세대 이후 자손의 수

table = [0]*(n+1) # 각각 AaBb가 index개 일 확률 표

# i는 0부터 e는 n부터 시작해서 확률 계산 수 table에 대입
for i, e in zip(range(0, n+1), range(n, -1, -1)):
    table[i] = (3/4)**e * (1/4)**i * combination(n, i)

print(sum(table[N:]))

