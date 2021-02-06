'''
<21.02.01>

『목표』
⊙ 파이썬 알고리즘(3)
- 정다면체 알고리즘 

『결과』
- 리스트와 for문 사용하여 나올 수 있는 눈의 합 확률 계산
'''
# 정다면체

n, m = map(int, input().split())
cnt = [0]*(n+m+5)  # +5는 넉넉하게 하기 위함

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

max = max(cnt)

for i in range(len(cnt)):
    if cnt[i] == max:
        print(i, end=' ')
