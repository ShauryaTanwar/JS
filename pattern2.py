# Time complexity: n * (n+1) / 2

y = ""
for x in range(6):
    for z in range(x):
        y = y + "*"
    print(y)
    y = ""