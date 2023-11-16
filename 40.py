# 정수 2개 입력받아 나눈 몫 계산
# 입력 : 2개의 정수(a, b)가 공백으로 구분되어 입력
# 출력 : a를 b로 나눈 몫을 출력

a, b = input().split()
c = int(a) // int(b)
print(c)