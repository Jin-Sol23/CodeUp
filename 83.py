# 종합 - 빛 섞어 색 만들기
# 입력 : 빨녹파(r,g,b) 각 빛의 가짓수가 공백을 두고 입력됨
# 출력 : 만들 수 있는 rgb 색의 정보를 오름차순으로 줄을 바꿔
# 모두 출력하고, 마지막에 그 개수를 출력

r, g, b = map(int, input().split())

for i in range(r): 
    for j in range(g):
        for k in range(b):
            print(i, j, k)
print(r*g*b)

# map(적용할 함수, 순회 가능한 객체)
# 순회 가능한 객체의 각 원소에 지정한 함수를 각각 적용하여
# 결과를 반환하는 함수          