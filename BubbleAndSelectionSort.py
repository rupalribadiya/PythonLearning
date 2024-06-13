
def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if(list[j] > list[j + 1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

def selectionSort(list):
    for i in range(len(list)-1):
        minpos = i;
        for j in range(i, len(list)):
            if(list[j] < list[minpos]):
                minpos = j
        if(list[minpos] != list[i]):
            temp = list[i]
            list[i] = list[minpos]
            list[minpos] = temp
    return list


list = [2,4,6,8,7,5,3,9, 0,45,99,78,56]
# print(bubbleSort(list))
print(selectionSort(list))