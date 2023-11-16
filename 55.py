# 논리연산 - 하나라도 참이면 참 출력
# 입력 : 2개의 정수가 공백을 두고 입력됨
# 출력 : 하나라도 참일 경우 True 출력, 그 외는 False 출력

a, b = input().split()
print(bool(int(a)) or bool(int(b)))