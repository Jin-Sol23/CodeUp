# 논리연산 - 참/거짓이 서로 같을 때만 참 출력
# 입력 : 2개의 정수가 공백을 두고 입력됨
# 출력 : 두 값의 True/False 값이 서로 같을 경우만 True 출력,
# 그 외의 경우는 False 출력

a, b = input().split()
c = int(a)
d = int(b)
print(bool(not c) and (not d) or bool(c and d))