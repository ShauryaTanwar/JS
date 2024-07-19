a = [34, 32, 35, 1, 1] # Change Array for testing
sLargest = -1
largest = a[1]

for num in a:
    if num < largest and num > sLargest:
        sLargest = num
    if num > largest:
        sLargest = largest
        largest = num

print(sLargest)