'''
비트(bit) : 1, 0
바이트(byte) : 비트 8개, 의미 있는 정보 하나를 표현하는 최소단위
첫번째 비트는 부호를 나타냄, 0=양수, 1=음수
1 bit = 8 byte

실수 값을 비트시프트 연산하면 오류 발생

n = 10 일 때,
print(n<<1) 10을 2배 한 값 = 20
print(n>>1) 10을 반으로 나눈 값 = 5
print(n<<2) 10을 4배 한 값 = 40
print(n>>2) 10을 반으로 나눈 값 = 2
'''

# 정수 1개 입력받아 2배 곱해 출력
# 입력 : 정수 한 개를 입력
# 출력 : 2배 곱한 정수를 출력

n = input()
n = int(n)
print(n<<1)