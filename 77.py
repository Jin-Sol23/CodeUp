# 종합 - 짝수 합 구하기
# 입력 : 정수 1개가 입력됨
# 출력 : 1부터 그 수까지 짝수만 합해 출력


n = input()
n = int(n)
s = 0
for i in range(1, n+1):
    if i%2 == 0:
        s += i
print(s)
