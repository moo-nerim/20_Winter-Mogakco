'''
<21.01.11>

『목표』
⊙ 파이썬 기초 문법 복습하기(3) 

『결과』
- 문자열과 내장함수 사용하여 문자열 역순 출력
- 문자 개수 세기
'''

'''
문자열과 내장함수
'''
msg = "It is Time"
print(msg.upper())  # upper() => 모두 대문자
print(msg.lower())  # lower() => 모두 소문자

tmp = msg.upper()
print(tmp.find('T'))  # find() => index
print(tmp.count('T'))  # count() => T 개수 셈
print(msg[:2])  # 처음부터 index 2 전까지 추출
print(msg[3:5])
print(len(msg))  # len() => 문자열 길이

# (1)
for i in range(len(msg)):
    print(msg[i], end='')
print()

# (2)
for x in msg:
    print(x, end='')
print()

# 문자열 관련 함수
for x in msg:
    if x.isupper():  # isupper() => 대문자면, islower() => 소문자면
        print(x, end='')
print()

for x in msg:
    if x.isalpha():  # isalpha() => 알파벳만 O, 공백 X
        print(x, end='')
print()

# 아스키번호
tmp = 'AZ'
for x in tmp:
    print(ord(x))  # ord() => 아스키번호 출력 A(65) ~ Z(90)

tmp = 'az'
for x in tmp:
    print(ord(x))  # ord() => 아스키번호 출력 a(97) ~ z(122)

tmp = 65
print(chr(tmp))  # chr() => 아스키번호에 대응하는 문자 출력
