# count 함수를 활용해서 더 간편하게
# 파일을 불러오는 기능까지 추가

import sys

file = open(sys.argv[1], 'r')
data = file.read()

A = data.count('A')
C = data.count('C')
G = data.count('G')
T = data.count('T')

print(A, C, G, T)
