import itertools
import math

n = int(input())

n_list = [i for i in range(1, n+1)]

# per_list, pro_list를 서로 곱해주어서 답을 얻는다.
per_list = list(itertools.permutations(n_list))
pro_list = list(itertools.product([-1, 1], repeat=n))

# per_list와 pro_list의 데카르트 곱
perpro_list = list(itertools.product(pro_list, per_list))

# 터미널 공간 부족으로 파일에다가 적기
# print(perpro_list)
# perpro_list에 있는걸 한 리스트씩 곱해서 print하기
with open('answer.txt', 'w', encoding='utf-8') as f:
    f.write(f'{len(perpro_list)}')
    f.write('\n')
    for i in range(len(perpro_list)):
        cursor = perpro_list[i]
        output = []
        for a in range(len(cursor[0])):
            output.append(cursor[0][a]*cursor[1][a])
        f.write(' '.join(map(str, output)))
        f.write('\n')

