# 논리연산 - 참/거짓이 서로 다를 때만 참 출력하기
# 입력 : 2개의 정수가 공백을 두고 입력
# 출력 : 두 값의 True/ False 값이 서로 다를 경우만 True 출력,
# 그 외 경우에는 False 출력

a, b = input().split()
c = int(a)
d = int(b)
print(bool(c and (not d) or ((not c) and d)))