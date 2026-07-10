import sys

# 10번 fastq format -> dic 코드 사용
dic = {}
cursor = ''
with open(sys.argv[1]) as f:
    for line in f:
         line = line.strip()
         
         if line.startswith('>'):
              cursor = line
              dic[cursor] = ""
         else:
              dic[cursor] += line

n = len(dic[cursor])


for i in range(n, 0, -1):
     a = 0
     # 문자열 안에서 뽑을 수 있는거 다 뽑기(3개의 문자 경우의 수 전체)
     while True:
          state = 1
          if a+i > n: # out of range면 뽑을 수 있는거 다 뽑았기 때문에 끝내기
               break
          # 다른 문자열에 존재하는지 일일히 확인
          for key in dic: 
               if dic[key].find(dic[cursor][a:a+i]) == -1:
                    state = 0
                    break

          # 만약에 break 없이 state = 1이 유지되었다면 print 하고 끝낸다.
          if state == 1:
               print(dic[cursor][a:a+i])
               sys.exit()

          # 다른 Motif 설정하기
          a += 1
          
# 이후엔 suffix tree / hash 를 활용해서 더 효율적인 코드를 짤 수 있음
# MEME suite에 관련 도구 있음