# rosalind
https://rosalind.info/users/songyun/
# Rosalind Solutions

바이오인포매틱스 알고리즘 학습 기록

## Bioinformatics Stronghold

| 제목 | 난이도 | 핵심 개념 | 문제 내용 | 날짜 | after work/algorithms | 
|---|---|---|---|---|:---:|
| 1. Counting DNA Nucleotides | ☆☆☆ | 문자열 카운팅, dict | DNA의 A,C,G,T 를 각각 세는 코드 | 26.07.01 | |
| 2. Transcribing DNA into RNA | ☆☆☆ | 문자열 치환 | RNA를 DNA로 바꾸는 코드 | 26.07.01 | |
| 3. Complementing a Strand of DNA | ★☆☆ | 문자열 역방향, 상보결합 매핑 | DNA의 상보결합 계산| 26.07.02 | |
| 4. Rabbits and Recurrence Relations | ★☆☆ | 피보나치, 재귀/반복 점화식 | 피보나치 수열 계산 | 26.07.02 | DP |
| 5. Computing GC Content | ★☆☆ | 문자열 파싱, 비율 계산, max | GC content 계산 후 max 출력 | 26.07.03 | |
| 6. Counting Point Mutations | ☆☆☆ | 문자열 비교, 해밍거리 | point mutation 계산 | 26.07.03 | |
| 7. Mendel's First Law | ★★☆ | 조건부 확률, 경우의 수 | 우성 표현형일 확률 계산 |26.07.04 | |
| 8. Translating RNA into Protein | ☆☆☆ | dict 매핑, 코돈 테이블 | RNA를 protein string으로 변환 | 26.07.04 | |
| 9. Finding a Motif in DNA | ★☆☆ | 문자열 탐색, 슬라이딩 윈도우 | 동일한 DNA 구간 찾기 | 26.07.04 | |
| 10. Consensus and Profile | ★☆☆ | 행렬 연산, 빈도 계산 | 여러 개의 DNA string에서 consensus 찾기 | 26.07.04 | |
| 11. Mortal Fibonacci Rabbits |★★★ | 동적 프로그래밍, 점화식 | mortal fibonacci 계산 | 26.07.05 | DP |
| 12. Overlap Graphs | ★☆☆ | 문자열 접두사/접미사, 그래프 | 끝쪽-앞쪽이 곂치는 dna 출력 | 26.07.05 | |
| 13. Calculating Expected Offspring | ☆☆☆ | 기댓값, 확률 계산 | 우성 표현형 예측값 구하기 | 26.07.05 | |
| 14. Finding a Shared Motif | ★★★ | Longest Common Substring | 여러개의 dna string에서 최대 motif 찾기 | 26.07.05 | suffix tree / hash <br> MEME suite |
| 15. Independent Alleles | ★★☆ | 이항분포, 조합, 멘델 유전법칙 | k 세대 이후 AaBb의 개수 구하기 | 26.07.05 | |
| 16. Finding a Protein Motif | ★★☆ | Uniprot, regex, Requests | Uniprot 이용해서 단백질의 motif index 찾기 | 26.07.06 | Unipron | 
| 17. Inferring mRNA from Protein | ★☆☆ | Modular Arithmetic | 단백질 -> 아미노산 으로 거꾸로 번역할 때의 경우의 수 | 26.07.06 | |
| 18. Open Reading Frames | ★★★ | ORF | DNA string에서 가능한 ORF 출력 | 26.07.08 | |
| 19. Enumerating_Gene_Orders | ★★★ | Enumerating | 가능한 순열 모두 출력 | 26.07.08 | permutations |
| 20. Calculating Protein Mass | ☆☆☆ | Residue Mass | 아미노산 서열을 통해 단백질의 질량 출력 | 26.07.09 | |
| 21. Locating Restriction Sites | ★★☆ | Reverse palindrome | Reverse Palindrome을 찾아 출력 | 26.07.09 | recursion보다 <br> 반복문이 더 직관적 |
| 22. RNA_Splicing | ★☆☆ | intron, exons | DNA에서 intron 제거후 번역 | 26.07.10 |  |
| 23. Enumerating k-mers Lexicographically | ★☆☆ | Enumerating | 순열 만든 후 sort | 26.07.10 | permutations |
| 24. Longest Increasing Subsequence | ★★★ | DP, LIS | 수열에서 최장 증가 부분수열 찾기 | 26.07.12 | LIS, 더 효율화 가능 |
| 25. Genome Assembly as Shortest Superstring | ★★★ | genome sequencing | substring으로 superstring 만들기(게놈 시퀀싱) | 26.07.12 | 더 readable 하게, 나중에 develop |
| 26. Perfect Matchings and RNA Secondary Structures | ★☆☆ | perfect matching | RNA folding의 가짓수 구하기 | 26.07.13 | |
| 27. Partial Permutations | ☆☆☆ | partial permutation | 부분순열 계산하기 | 26.07.13 | |
| 28. Introduction to Random Strings | ☆☆☆ | random | 특성 GCcontenst에서 특정 motif 나올 확률 구하기 | 26.07.15 | |
| 29. Enumerating Oriented Gene Orderings | ★☆☆ | itertools(permutation, product) | 부호 있는 순열 전체 열거 | 26.07.17 | |
| 30. Finding a Spliced Motif | ☆☆☆ | subsequence | subsequence 만들기 | 26.07.17 |  |
| 31. Transitions and Transversions | ☆☆☆ | transition/transversion ratio | transition/transversion ratio 구하기 | 26.07.18 |  |
| 32. Completing a Tree | ☆☆☆ | tree | tree 만들기 위한 최소한의 edges 구하기 | 26.07.18 |  |
| 33. Catalan Numbers and RNA Secondary Structures | ★☆☆ | Catalan number | RNA의 염기 쌍 조건이 추가된 Catalan number 구하기| 26.07.19 | interval DP |






