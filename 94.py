# 리스트 - 이상한 출석 번호 부르기3
# 입력 : 번호를 부른 횟수(n, 1~10000)가 첫 줄에 입력됨
# n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력됨
# 출력 : 출석을 부른 번호 중에 가장 빠른 번호를 출력함

# 다른 사람 코드
n = int(input())
k = list(map(int,input().split()))
a=k[0]
for i in range(n):
    if(a>k[i]):
        a=k[i]
print(a)


# 정답 코드
n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])

min = k[0]
for i in range(0,n):
    if k[i] < min:
        min = k[i]
print(min)