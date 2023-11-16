# 리스트 - 이상한 출석 번호 부르기1
# 입력 : 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력됨
# 두 번째 줄에 무작위로 부른 n개의 번호(1~23)가 공백을 두고 순서대로 입력됨
# 출력 : 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])
    
d = []
for i in range(24):
    d.append(0)
for i in range(n):
    d[a[i]] += 1
for i in range(1, 24):
    print(d[i], end=' ')