# 파일 읽어오기
import sys

with open(sys.argv[1]) as f:
    DNA1 = f.readline().strip()
    DNA2 = f.readline().strip()

# 출력값 초기화
Hamming_distance = 0

# DNA1 DNA2 비교하기
for i in range(len(DNA1)):
    if DNA1[i] != DNA2[i]:
        Hamming_distance += 1

print(Hamming_distance)
