h, w = input().split()
h = int(h) # 격자판 세로의 크기
w = int(w) # 격자판 가로의 크기
n = int(input()) # n = 놓을 수 있는 막대의 개수
l, d, x, y = map(int, input().split())
# l = 막대 길이
# d = 막대 방향, d=0이면 가로, d=1이면 세로
# x = 세로축 좌표
# y = 가로축 좌표

a = [[0 for i in range(h)]for j in range(w)]