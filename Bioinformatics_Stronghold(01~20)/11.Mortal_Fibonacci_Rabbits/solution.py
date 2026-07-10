# 처음에는 수학적으로 점화식을 만들려고 했는데 규칙 발견이 쉽지 않아, 블로그 참고하여 리스트를 만들어 해결함.

n, m = map(int, input().split())

age = [1] + [0] * (m-1) # 리스트로 index[0]은 0살 [1]은 1살 이렇게 현재 존재하는 토끼수를 나타냄

for i in range(2,n+1):
    age = [sum(age[1:])] + age[:-1] # 태아난 토끼를 sum, 마지막 index을 삭제(죽은토끼)

print(sum(age))