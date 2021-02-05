'''
<21.01.27>

『목표』
⊙ 파이썬 알고리즘(2)
- 대표값 알고리즘 

『결과』
- 절댓값 abs()를 사용하여 평균 점수 계산
'''
# 대표값

n = int(input())
a = list(map(int, input().split()))

average = round(sum(a)/n)
# print(average)

min = float('inf')
res = 0

for idx, x in enumerate(a):  # enumerate() => (index, value) 쌍으로
    tmp = abs(x-average)  # abs() => 절댓값
    if tmp < min:
        min = tmp
        score = x  # 점수
        res = idx+1  # index
    elif tmp == min:
        if score < x:
            score = x
            res = idx+1
print(average, res)
