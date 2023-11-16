n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])
    s = k.index(min(k))
print(s[0])