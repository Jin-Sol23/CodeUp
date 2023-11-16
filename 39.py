# 실수 2개 입력받아 거듭제곱 계산
# 입력 : 2개의 실수(f1, f2)가 공백으로 구분되어 입력
# 계산 : f1를 f2번 거듭제곱한 값을 출력

a, b = input().split()
c = float(a) ** float(b)
print(c)