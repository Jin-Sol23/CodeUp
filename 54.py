# 논리연산 - 둘 다 참일 경우만 참 출력하기
# 입력 : 2개의 정수가 공백을 두고 입력됨
# 출력 : 둘 다 True 일 경우에만 True 출력, 그 외는 False 출력

a, b = input().split()
print(bool(int(a)) and bool(int(b)))