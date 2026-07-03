import sys

# 개월수(n), 자손 수(k) input 받기
n, k = map(int, input().split())

# 초기값 설정
Fibo = [1,1]

if n < 3:
    print(1)
    sys.exit()

else:
    for i in range(2, n):
        Fibo.append(Fibo[i-1] + k*Fibo[i-2])
    
print(Fibo[n-1])

