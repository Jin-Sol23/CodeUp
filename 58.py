# 논리연산 - 둘 다 거짓일 경우만 참 출력
# 입력 : 2개의 정수가 공백을 두고 입력됨
# 출력 :

a, b = input().split()
c = int(a)
d = int(b)
print(not(c or d))