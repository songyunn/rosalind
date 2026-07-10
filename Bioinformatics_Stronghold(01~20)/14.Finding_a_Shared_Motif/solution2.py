import sys

# 파일 읽기 (dic에 데이터 저장)
dic = {}
cursor = ''
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line: continue
        if line.startswith('>'):
            cursor = line
            dic[cursor] = ""
        else:
            dic[cursor] += line

# 모든 서열 중 하나를 기준으로 잡음 (루프에서 cursor를 그대로 사용)
n = len(dic[cursor])

# i는 모티프의 길이
for i in range(n, 0, -1):
    a = 0
    # 길이가 i인 모티프를 모두 검사 (a의 범위는 0부터 n-i까지)
    while a + i <= n: 
        state = 1
        # 현재 기준 모티프
        target_motif = dic[cursor][a : a + i]
        
        # 모든 key에 대해 확인
        for key in dic:
            if target_motif not in dic[key]:
                state = 0
                break
        
        if state == 1:
            print(target_motif)
            sys.exit()
        
        a += 1