'''
<21.01.06>

『목표』
⊙ 파이썬 기초 문법 복습하기(2) 

『결과』
- 조건문, 반복문 문법 학습
- 중첩반복문을 사용하여 별 모양 찍기
'''

'''
반복문(for, while)

a = range(1, 11)
print(list(a))

for i in range(10):
    print(i)  # 0 1 2 ... 9

for i in range(10, 0, -1): # 1씩 작아짐
    print(i)  # 10 9 8 ... 1
'''
# while문

i = 1
while i <= 10:
    print(i)
    i = i+1  # 1씩 증가

i = 10
while i >= 1:
    print(i)
    i = i-1  # 1씩 감소

# 무한반복
i = 1
while True:
    print(i)
    if i == 10:
        break
    i += 1

# continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
    
# for-else
for i in range(1, 11):
    print(i)
    if i==5:
        break
else:
    print(11) # break를 당해 출력 X    

'''
반복문을 이용한 문제풀이
 1) 1부터 N까지 홀수 출력
 2) 1부터 N까지의 합 구하기
 3) N의 약수 출력
'''
# 1)
n = int(input())  # input()은 str이므로 꼭 형변환!
for i in range(1, n+1):
    if i % 2 != 0:
        print(i)

# 2)
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# 3)
for i in range(1, n+1):
    if n % i == 0:
        print(i , end=' ') # 줄 안바꿈

'''
중첩 반복문(2중 for문)
'''
for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()


