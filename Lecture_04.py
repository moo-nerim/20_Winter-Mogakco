'''
<21.01.13>

『목표』
⊙ 파이썬 기초 문법 복습하기(4) 
- 리스트와 내장함수

『결과』
- 리스트와 튜플 사용하여 생성
- 리스트에 원소 추가, 삭제, 변경 
'''

'''
리스트와 내장함수(1)
'''
import random as r  # random

b = list()  # 리스트 생성
print(b)

a = [1, 2, 3, 4, 5]  # 리스트 생성
print(a)
print(a[0])  # 1

b = list(range(1, 11))
print(b)

c = a+b  # 리스트 합침
print(c)

# 리스트 내장함수
a.append(6)  # append() => 원소 추가
print(a)

a.insert(3, 7)  # insert() => 특정 index에 원소 추가
print(a)

a.pop()  # pop() => 맨 마지막 원소 꺼내서 삭제
print(a)
a.pop(3)
print(a)

a.remove(4)  # remove() => 특정 값 찾아서 삭제
print(a)

print(a.index(5))  # 특정 값에 해당하는 index 출력

a = list(range(1, 11))
print(a)
print(sum(a))  # sum() => a에 있는 모든 원소의 합
print(max(a))  # max() => 인자값 중 가장 큰 원소의 값
print(min(a))  # min() => 인자값 중 가장 작은 원소의 값
print(min(7, 5))  # 5

print(a)
r.shuffle(a)  # a값 무작위로 섞음
print(a)
a.sort()  # sort() => 오름차순 정렬
print(a)
a.sort(reverse=True)  # 내림차순 정렬
print(a)
a.clear() # clear() => Remove all items from list.(빈 리스트)
print(a)

'''
리스트와 내장함수(2)
'''
a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()  # 줄바꿈

for x in a:
    if x % 2 != 0:  # 홀수만 출력
        print(x, end=' ')
print()

for x in enumerate(a):  # enumerate() => (index, value) 쌍으로 접근
    print(x)

b = (1, 2, 3, 4, 5)  # tuple
print(b[0])
# b[0]=7 // error => tuple은 원소값 변경 X, 리스트는 변경 O

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(60 > x for x in a):  # all 모두 참일 경우 => true
    print("YES")
else:
    print("NO")

if any(15 > x for x in a):  # any 한개라도 참일 경우 => true
    print("YES")
else:
    print("NO")