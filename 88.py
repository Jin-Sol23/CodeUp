# 종합 - 수 나열하기1
# 입력 : 시작값(a), 등차값(d), 몇 번째 수인지 의미하는 정수(n)
# a, d, n이 공백을 두고 입력됨
# 출력 : n번째 수를 출력함

a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

print(a+d*(n-1)) # 검색

# 정답
a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

s = a
for i in range(2, n+1):
    s += d
print(s)
