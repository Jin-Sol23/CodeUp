# 정수 2개 입력받아 자동 계산
# 입력 : 정수 2개가 공백을 두고 입력
# 출력 : 합, 차, 곱, 몫, 나머지, 나눈 값(실수, 소수점 이하 둘째 짜리)을 순서대로 다른 줄에 출력

a, b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))
print(format(int(a)/int(b), ".2f"))
