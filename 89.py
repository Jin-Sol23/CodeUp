# 종합 - 수 나열하기2
# 입력 : 시작값(a), 등비값(r), 몇번째인지 나타내는 정수(n)
# a, r, n이 공백을 두고 입력됨
# 출력 : n번째 수를 출력함

a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

s = a
for i in range(2, n+1):
    s = s * r
print(s)