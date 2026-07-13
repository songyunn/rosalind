import sys

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

answer = next(iter(dic.values())) # 첫번째 value부터 시작하기
first_key = list(dic.keys())[0] # 첫번째 dic는 사용했으니 삭제하기
del dic[first_key]

# 이걸 while 문에 넣어서 끝날때까지 계속 실행하기
while True:
    for i in range(n-1, n//2-1, -1):

        dna_sliced_left = answer[:i] # 왼쪽부터 진행 이후에 오른쪽 재는 과정도 똑같이 만들기

        result_left = [val for val in dic.values() if dna_sliced_left in val] # 길이 i만큼 slicing한 문자열이 있는 곳을 확인

        # ---------------------------- 왼쪽 문자열 합치기, 사용한 key 지우기 ------------------------------ #
        key_string = ''
        overlap = 0
        for string in result_left:
            # 제일 많은 정보를 줄 수 있는 한개만 남겨두고 합치기
            a = string.find(dna_sliced_left)
            if a > overlap:
                key_string = string
                overlap = a
        answer = key_string[:overlap] + answer # 가장 overlap이 큰 값으로 합치기

        # 사용한 key 모두 삭제
        del_list = []
        for key, dna in dic.items():
            if dna in result_left:
                del_list.append(key)
        
        for key in del_list:
            del dic[key]
        
        if len(result_left) != 0:
            break
        # -------------------------------------------------------------------------- #

    for i in range(n-1, n//2-1, -1):
        dna_sliced_right = answer[-i:] # 오른쪽 진행

        result_right = [val for val in dic.values() if dna_sliced_right in val] # 길이 i만큼 slicing한 문자열이 있는 곳을 확인

        # ---------------------------- 오른쪽 문자열 합치기, 사용한 key 지우기 ------------------------------ #
        key_string = ''
        overlap = 100000
        for string in result_right:
            # 제일 많은 정보를 줄 수 있는 한개만 남겨두고 합치기
            a = string.find(dna_sliced_right)
            if a < overlap:
                key_string = string
                overlap = a
        answer = answer + key_string[overlap + i:] # 가장 overlap이 큰 값으로 합치기

        # 사용한 key 모두 삭제
        del_list = []
        for key, dna in dic.items():
            if dna in result_right:
                del_list.append(key)
        for key in del_list:
            del dic[key]
        # -------------------------------------------------------------------------- #
        if len(result_right) != 0:
            break



    if len(result_left) == 0 and len(result_right) == 0:
        break

print(answer)