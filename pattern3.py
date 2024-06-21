a = [1, 2, 3, 4, 5]
y = ""
for x in range(6):
    for z in range(x):
        y = y + str(a[z])
    print(y)
    y=""