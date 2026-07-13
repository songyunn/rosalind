import sys

with open(sys.argv[1]) as f:
    dna = ''.join(f.read().split('\n')[1:])

rna_complement = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

def matching(string):

     # 모두 다 짝을 찾았다면 answer 1 추가하고 종료
    if len(string) == 0:
        # print("find")
        return 1
    
    # base paris가 맞는 index 다 모아두기
    result = [index for index in range(1, len(string)) if string[index] == rna_complement[string[0]]] 
    # print(result)

    # string은 남았는데 짝을 못 찾았다면 그냥 종료
    if len(result) == 0:
        return 0

    total_count = 0
    # 짝 하나 찾고 남은 string으로 함수 다시 실행
    for i in result:
        next_string = string[1:i] + string[i+1:]
        total_count += matching(next_string)
    
    return total_count

print(matching(dna))
