a, b = map(int, input().split())

answer = 1
for i in range(b):
    answer *= a
    answer %= 1000000
    a -= 1

print(answer)