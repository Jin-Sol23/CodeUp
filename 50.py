# 정수 2개 입력받아 비교하기
# 입력 : 2개의 정수(a, b)가 공백을 두고 입력
# 출력 : b가 a보다 크거나 같은 경우, 그렇지 않은 경우 출력

a, b = input().split()
a = int(a)
b = int(b)
print(b>=a)