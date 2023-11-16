
# [기초-입출력] 정수 2개 입력받아 그대로 출력하기2(설명)
# 입력 : 2개의 정수가 공백으로 구분되어 입력된다.
# 출력 : 입력된 두 정수를 줄을 바꿔 출력한다.

# 1
a, b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)

# 2
a, b = map(int, input().split())
print(a)
print(b)


##ddd