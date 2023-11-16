# 정수 2개 입력받아 거득제곱 계산
# 입력 : 2개 정수(a, b)가 공백으로 구분되어 입력
# 출력 : a를 b번 거듭제곱한 값을 출력

a, b = input().split()
c = int(a) ** int(b)
print(c)