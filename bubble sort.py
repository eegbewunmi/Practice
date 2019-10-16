#Bubble sort Algorithm
def bubble_sort(list):
    #i=1
    for i in range(len(list)):
        #Don't check the last elements since they will be in place after each iteration (they will be the highest values)
        for j in range(0, len(list)-1-i):
            if list[i] > list [i+1]:
            #swap them
                list[i], list[i+1] = list[i+1], list[i]
    return list


list1=[3,0,8,7,5]
bubble_sort(list1)
print (list1)
#print (bubble_sort(list1))
