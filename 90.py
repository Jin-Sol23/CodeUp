# 종합 = 수 나열하기3 (수열)
# 입력 : 시작값(a), 곱할값(m), 더할값(d), 몇번째인지 나타내는 정수(n)
# a, m, d, n이 공백을 두고 입력됨
# 출력 : n번째 수를 출력함

a, m, d, n = map(int, input().split())

for i in range(2, n+1):
    a = a * m + d
print(a)