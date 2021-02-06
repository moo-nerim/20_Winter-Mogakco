'''
<21.02.03>

『목표』
⊙ 파이썬 알고리즘(4)
- 자릿수의 합 알고리즘 

『결과』
- 10의 몫과 나머지를 사용하여 합 계산
- str로 변환한 뒤 접근하고 int로 다시 변환하여 합 계산
'''
# 자릿수의 합

n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x//10
    return sum

''' 
(2) str로 변환
def digit_sum(x):
    sum = 0
    for i in str(x): # 문자열 하나씩 접근
        sum += int(i)
    return sum     
'''

max = 0

for i in a:
    total = digit_sum(i)
    if max < total:
        max = total
        res = i
print(res)
