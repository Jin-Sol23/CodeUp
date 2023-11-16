# 종합 - 주사위 2개 던지기
# 입력 : 서로 다른 주사위 2개의 면의 개수 n, m이 공백을 두고 입력됨
# 단, n, m은 10이하의 자연수
# 출력 : 나올 수 있는 주사위의 숫자를 한 세트씩 줄을 바꿔 모두 출력

n, m = input().split()
n = int(n)
m = int(m)

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)