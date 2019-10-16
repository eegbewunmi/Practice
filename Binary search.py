#Binary search Algorithm
def Binary_search(list, value):
    list.sort()
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int ((low+high)/2)
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return "Value not found in list"


list1 = [2, 7, 6, 3, 20, 16 ]
v1 = 16
v2 = 18

print (Binary_search(list1, v1))
print (Binary_search(list1, v2))
