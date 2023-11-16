# 조건/선택실행구조 - 정수 3개 입력받아 짝수만 출력
# 입력 : 3개의 정수가 공백을 두고 입력됨
# 출력 : 짝수만 순서대로 줄 바꿔 출력

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a%2==0 :
    print(a)
if b%2==0 :
    print(b)
if c%2==0 :
    print(c)