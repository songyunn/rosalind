k, m, n = map(int, input().split())


n_n = n*(n-1)/2
m_n = m*n/2

a = (k+m+n)*(k+m+n-1)/2

print(1 - (n_n+m_n)/a)

print(n_n, m_n, a)