[MIT] 파이썬을 이용한 알고리즘의 이해 

# Contents 
- Algorithmic thinking: peak finding
- Sorting&trees: Event simulation 
- Hashing: Genome comparison
- Numerics: RSA encryption (RSA 암호화. https 쓸 경우 백엔드에서 RSA가 쓰임)
- Graphs: Rubik's cube 
- Shortest Paths: Caltech -> MIT
- Dynamic Programming: Image Compression 
- Advance topics: .... 
<br>
<br>
<br>

# 1. Introduction
## 1-1 Peak finding
### one-dimensional version
- divide&conquer(분할정복) 
- T(n) : "work" algo does on input of size n 
- 알고리즘 실행시간 T(n): n의 입력을 받았을 때 이 알고리즘이 하는 일의 양
- T(n) = T(n/2) + θ(1)  
- base case: T (1) = θ(1 ) 
- T(n) = θ(1) + ... + θ(1)  = θ( log2 n)


### two-dimensional version
- Greedy Ascent algorithm(탐욕 상승 알고리즘): θ(nm) Complexity(비효율적) 

- T(n, m) = T(n, m/2) + θ(n)
- base case: T(n, 1) = θ(n) 
- T(n, m) = θ(n) + ... + θ(n) = θ(nlog2 m)


## 1-2 Models of Computation
### 표기법
- 빅오 표기법(O(n)): 최악의 경우
- 빅오메가 표기법(Ω(n)): 최선의 경우
- 빅세타 표기법(θ(n)): 평균의 경우(빅오, 빅오메가가 같을 때...)

### 강의노트에서
- 각 연산마다 시간 얼마 걸리는지 . 
