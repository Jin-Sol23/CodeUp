# 3항연산 - 정수 2개 입력받아 큰 값 출력
# 입력 : 두 정수가 공백을 두고 입력됨
# 출력 : 두 정수 중 큰 값을 10진수로 출력

a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a>=b) else b)
print(c)

# 3개의 요소로 이루어지는 3항 연산
# x if C else y
# C : True, False 를 평가할 조건식 또는 값
# x : C의 평가 결과가 True 일 때 사용할 값
# y : C의 평가 결과가 True가 아닐 때 사용할 값