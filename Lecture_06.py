'''
<21.01.25>

『목표』
⊙ 파이썬 알고리즘(1)
- K번째 수 알고리즘 풀기

『결과』
- K번째 약수 알고리즘 해결
- K번째 수 알고리즘 해결
- K번째 큰 수 알고리즘 해결(△)
'''
# K번째 약수

n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else: # for-else문
    print(-1)

# K번째 수
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))

    a = a[s-1:e]  # s번째 ~ e번째
    a.sort()  # 오름차순 정렬
    print('#', t+1, a[k-1])
    # print("#%d %d" % (t+1, a[k-1]))
