# 종합 - 3 6 9 게임의 왕이 되자
# 입력 : 30보다 작은 정수 1개 입력됨 (1~29)
# 출력 : 1 부터 그 수까지 순서대로 공백을 두고 수를 출력,
# 3, 5, 9가 포함 되어 있는 수인 경우, 그 수 대신 영문 대문자 X를 출력

n = int(input())

for i in range(1, n+1):
    if i % 10 == 3:
        print("X", end=' ')
    elif i % 10 == 6:
        print("X", end=' ')
    elif i % 10 == 9:
        print("X", end=' ')
    else:
        print(i, end=' ')