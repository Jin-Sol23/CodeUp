# 실수 2개 입력받아 나눈 결과 계산
# 입력 : 2개의 실수가 공백으로 구분되어 입력
# 출력 : 나눈 결과를 소수점 이하 넷째 자리에서 반올림하여 소수점 세 번째 자리까지 출력

f1, f2 = input().split()
c = float(f1) / float(f2)
print(format(c, ".3f"))