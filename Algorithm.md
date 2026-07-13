# Algorithm Patterns


## 1. Dynamic Programming (동적계획법)

<br>

### 1-1. LIS (Longest Increasing Subsequence)
> 참고: &nbsp; https://www.geeksforgeeks.org/dsa/longest-increasing-subsequence-dp-3/<br>
등장 문제:&nbsp;24.LGIS

[첫번째 풀이 코드(오답)](./Bioinformatics_Stronghold(21~40)/24.Longest_Increasing_Subsequence/solution(ineffective,2^n).py): 시간 복잡도가 O(2^n)으로 러닝타임 오류
<br>
[2번째 풀이 코드](./Bioinformatics_Stronghold(21~40)/24.Longest_Increasing_Subsequence/solution.py): 시간 복잡도 O(n^3), 메모리 복잡도 O(N^2)
- dp_inc[i]는 data[i]를 마지막 원소로 하는 LIS 후보(subsequence 자체)를 저장한다. 
- 예: data = [5, 1, 4, 2, 3] → dp_inc = [[5], [1], [1,4], [1,2], [1,2,3]]
- dp_inc의 생성을 이중 반복문을 통해 data[i]를 이전 index와 비교해서 진행한다.
- 이 방식은 길이가 아닌 실제 수열을 저장하므로 이해는 쉽지만 공간 효율은 떨어진다 (O(n²)).
- **[after work]** 이분탐색(patience sorting) 등으로 O(n log n) 최적화 시도해보기.

<br>


### 📘 DP 문제

| 문제 | 패턴 | 메모 |
|---|---|---|
| 4. Rabbits and Recurrence Relations | 선형 점화식, O(n) | 가장 단순한 형태. dp[n] = dp[n-1] + dp[n-2]*k |
| 11. Mortal Fibonacci Rabbits | 상태 있는 DP | 나이별 개체 수를 배열/리스트로 추적 (DP의 시작점) |
| 14. Finding a Shared Motif | Longest Common Substring | 이후 suffix tree/array 사용하여 최적화 가능 |

<br>

---
## 2. Combinatorics & Enumeration (조합/열거)

### 📘 Combination & Enumeration 문제

| 문제 | 패턴 | 메모 |
|---|---|---|
| 19. Enumerating Gene Orders | permutation 생성 | itertools의 permutation과 동일, recursion에 current, remaining 으로 구현 |
| 23. Enumerating k-mers Lexicographically | permutation 생성 | 19번 함수 활용해서 구현 |