k, m, n = map(int, input().split())

# 전체 가능성에서 열성 표현형일 가능성 빼기
m_m = m*(m-1)/8
m_n = m*n/2
n_n = n*(n-1)/2
a = (k+m+n)*(k+m+n-1)/2

print(1 - (m_m+m_n+n_n)/a)