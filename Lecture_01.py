'''
<21.01.04>

『목표』
⊙ 파이썬 기초 문법 복습하기(1) 

『결과』
- 파이썬 설치 및 변수와 출력함수 학습
'''

'''
a=input("input number : ")
print(a)
'''

a, b = input("input number : ").split()
print(type(a)) # str
print(a+b) # 23

# (1)
a, b = input("input number : ").split()
a = int(a) # 2
b = int(b) # 3
print(a+b) # 5

# (2) map() 사용하여 정수화
a, b = map(int,input("input number : ").split()) 
print(a+b)  
print(a-b) 
print(a*b) 
print(a/b) 
print(a//b) # 몫
print(a%b)  # 나머지
print(a**b) # 거듭제곱