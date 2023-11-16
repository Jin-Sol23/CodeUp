# 비트단위논리연산 - 비트단위로 XOR 하여 출력
# 입력 : 2개의 정수가 공백을 두고 입력됨
# 출력 : 두 정수를 비트단위로 xor 계산을 수행한 결과를 10진수로 출력

a, b = input().split()
print(int(a) ^ int(b))

# ^ : 배타적 논리합, xor, circumflex/caret
# 서로 다를 때 1, 같으면 0