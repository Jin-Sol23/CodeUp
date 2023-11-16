# 2의 거듭제곱 배로 곱해 출력
# 입력 : 정수 2개(a, b)가 공백을 두고 입력됨
# 출력 : a를 2^b배 만큼 곱한 값을 출력

a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)