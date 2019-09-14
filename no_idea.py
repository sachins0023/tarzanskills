n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
h = 0
for i in arr:
    if i in a:
        h += 1
    elif i in b:
        h -= 1