# 3항연산 - 정수 3개 입력받아 가장 작은 값 출력
# 입력 : 3개의 정수가 공백으로 구분되어 입력됨
# 출력 : 가장 작은 값 출력

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a if a<b else b) if ((a if a<b else b)<c) else c)
