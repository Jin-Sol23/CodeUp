# 조건/선택실행구조 - 평가 입력받아 다르게 출력
# 입력 : 영문자 1개 입력됨
# 출력 : 문자에 따라 내용 출력
'''
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
'''

a = input()

if a == "A" :
    print("best!!!")
elif a == "B" :
    print("good!!")
elif a == "C" :
    print("run!")
elif a == "D" :
    print("slowly~")
else :
    print("what?")