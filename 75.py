# 반복실행구조 - 정수 1개 입력받아 그 수까지 출력
# 입력 : 정수 1개 입력됨
# 출력 : 0부터 그 수까지 줄 바꿔 한 개씩 출력

i = 0
a = input()
a = int(a)
while i <= a:
    print(i)
    i += 1