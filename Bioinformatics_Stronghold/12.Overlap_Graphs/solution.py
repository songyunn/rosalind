import sys

# 10번 fastq format -> dic 코드 사용
dic = {}
cursur = ''
with open(sys.argv[1]) as f:
    for line in f:
         line = line.strip()
         
         if line.startswith('>'):
              cursor = line
              dic[cursor] = ""
         else:
              dic[cursor] += line

# 이중 반복문으로 한개씩 비교하기
for key in dic:
     for c in dic:
        #   print(dic[key][-3:], dic[c][:3] ) # 디버깅용
          if key == c:
               continue
          if dic[key][-3:] == dic[c][:3]:
               print(key[1:], c[1:])