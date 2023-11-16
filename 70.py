# 조건/선택실행구조 - 월 입력받아 계절 출력
# 입력 : 월 의미하는 1개의 정수 입력
# 출력 : 계절 이름 출력

a = input()
a = int(a)

if a // 3 == 1 :
    print("spring")
elif a // 3 == 2 :
    print("summer")
elif a // 3 == 3 :
    print("fall")
else :
    print("winter")