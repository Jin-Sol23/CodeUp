# 조건/선택실행구조 - 정수 1개 입력받아 분류
# 입력 : 정수 1개 입력
''' 출력 :
음수, 짝수 = A
음수, 홀수 = B
양수, 짝수 = C
양수, 홀수 = D
'''

a = input()
a = int(a)

if a<0:
    if (a<0) and (a % 2 == 0):
        print("A")
    else: 
        print("B")
else:
    if (a>0) and (a % 2 ==0):
        print("C")
    else:
        print("D")