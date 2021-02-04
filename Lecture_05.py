'''
<21.01.18>

『목표』
⊙ 파이썬 기초 문법 복습하기(5) 
- 함수 사용

『결과』
- 소수 판별 함수 생성하여 적용
- 람다함수 사용하여 함수와 비교
'''

# 소수 판별
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]
# for x in a:
for x in range(len(a)):
    if isPrime(a[x]):
        print(a[x],end=' ')
        

'''
람다 함수

def plus_one(x):
    return x+1

print(plus_one(1))

plus_two = lambda x: x+2
print(plus_two(1))
'''


def plus_one(x):
    return x+1

a = [1, 2, 3]
print(list(map(plus_one, a)))  # map(함수명, 자료)
print(list(map(lambda x: x+1, a)))  # map(람다식, 자료)
