given = list(map(int, input().split(' ')))

# increasing subsequence 찾기
all_increasing_sub = []

# 첫 cursor는 0
def make_inc_subsequence(current, remaining, cursor):
    if len(remaining) != 0:
         make_inc_subsequence(current, remaining[1:], cursor) # 다음값이 더 크더라도 무시하는 상황 하나 만들기
         
         if cursor < remaining[0]:
            next_current = current + [remaining[0]]
            next_remaining = remaining[1:]
            next_cursor = remaining[0]
            make_inc_subsequence(next_current, next_remaining, next_cursor)
    
    if len(remaining) == 0:
        if current != None: # 아무것도 없을때 발생하는 오류 방지
            all_increasing_sub.append(' '.join(map(str, current)))

# 함수 실행
make_inc_subsequence([], given, 0)

# decreasing subsequence 찾기
all_decreasing_sub = []

# 첫 cursor는 0
def make_dec_subsequence(current, remaining, cursor):
    if len(remaining) != 0:
         make_dec_subsequence(current, remaining[1:], cursor) # 다음값이 더 크더라도 무시하는 상황 하나 만들기
         
         if cursor > remaining[0]:
            next_current = current + [remaining[0]]
            next_remaining = remaining[1:]
            next_cursor = remaining[0]
            make_dec_subsequence(next_current, next_remaining, next_cursor)
    
    if len(remaining) == 0:
        if current != None: # 아무것도 없을때 발생하는 오류 방지
            all_decreasing_sub.append(' '.join(map(str, current)))

# 함수 실행
make_dec_subsequence([], given, max(given) + 1)

print(max(given) + 1)
print(max(all_increasing_sub, key=len))
print(max(all_decreasing_sub, key=len))
print(all_increasing_sub)
print(all_decreasing_sub)