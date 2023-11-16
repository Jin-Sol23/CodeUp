# 조건/선택실행구조 - 점수 입력받아 평가 출력
# 입력 : 정수(0~100) 1개 입력됨
# 출력 : 평가 결과 출력
''' 평가 기준
90 ~ 100 : A
70 ~ 89 : B
40 ~ 69 : C
0 ~ 39 : D
'''

a = input()
a = int(a)

if a >= 90 :
    print("A")
elif (a >= 70) and (a < 90) :
    print("B")
elif (a >= 40) and (a < 70) :
    print("C")
else :
    print("D")