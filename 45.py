# 정수 3개 입력받아 합과 평균 출력
# 입력 : 정수 3개가 공백을 두고 입력
# 출력 : 합, 평균을 공백을 두고 출력, 평균은 소수점 둘째 자리까지 출력

a, b, c = input().split()
d = int(a) + int(b) + int(c)
e = d/int(3)
print(d, format(e, ".2f"))
