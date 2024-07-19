

def shiftArray(arr, num):
    for x in range(num):
        temp = arr[len(arr)-1]
        for i in range(len(arr)-1):
            arr[len(arr)-1-i]=arr[len(arr)-2-i]
        arr[0]=temp

testArray = [1, 2, 3, 4, 5, 6, 7]
shiftArray(testArray, 2)
print(testArray)