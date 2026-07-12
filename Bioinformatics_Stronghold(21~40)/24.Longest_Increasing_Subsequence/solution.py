import sys

with open(sys.argv[1]) as f:
    n = int(f.readline()) # 총 데이터의 개수
    data = list(map(int, f.readline().split())) # 데이터를 리스트로 받기 # int로 안 바꿔줘서 틀렸음

# -----------------------1. LIS -------------------------------------------#

# 각 index가 subsequence에서 마지막 숫자라고 할 때 가능한 문자열 저장
# 자기 자신으로 초기화
db_inc = [] 
for i in data:
    db_inc.append([i])


for i in range(n): # 각 index 전 인덱스들과 비교
    for j in range(i): 
        if data[i] > data[j]: # 이전 값들보다 더 크면 가져오기
            if len(db_inc[i]) <= len(db_inc[j]):
                db_inc[i] = db_inc[j] + [data[i]]

print(' '.join(map(str, max(db_inc, key=len))))

# -------------------------2. LDS-----------------------------------------#
            
# 각 index가 subsequence에서 마지막 숫자라고 할 때 가능한 문자열 저장
# 자기 자신으로 초기화
db_dec = [] 
for i in data:
    db_dec.append([i])


for i in range(n): # 각 index 전 인덱스들과 비교
    for j in range(i): 
        if data[i] < data[j]: # 이전 값들보다 더 크면 가져오기
            if len(db_dec[i]) <= len(db_dec[j]):
                db_dec[i] = db_dec[j] + [data[i]]

print(' '.join(map(str, max(db_dec, key=len))))