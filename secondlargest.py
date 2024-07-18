a = [1, 4, 9, 2, 6]
sLargest = -1
largest = a[1]

for num in a:
    if num < largest and num > sLargest:
        sLargest = num
    if num > largest:
        sLargest = largest
        largest = num

print(sLargest)