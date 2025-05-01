'''list = [67,23,707,332,324,-2]
print("MINIMUM Number From List is ", min(list))
print("MAXIMUM Number From List is ", max(list))'''

'''
list = [67,23,707,332,324,-2]
list.sort()
print("List After Sorted is : " ,list )
print(list[0])
print(list[-1])
'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
print("Array before sorted : ", arr )
bubble_sort(arr)
print("Sorted array:", arr)