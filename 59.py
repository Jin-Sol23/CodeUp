# 비트단위논리연산 - 비트단위로 NT 하여 출력
# 입력 : 정수 1개 입력됨
# 출력 : 비트 단위로 1 -> 0, 0 -> 1로 바꾼 후 그 값을 10진수로 출력

a = int(input())
print(~a)

# ~ : 틸드, tilde
# ~n = -n - 1
# -n = ~n + 1