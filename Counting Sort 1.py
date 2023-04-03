def countingSort(arr):
    aux_list = [0]*100
    for i in arr:
        aux_list[i] += 1
    return aux_list

print(countingSort([0,2,6,9,7,45,4,1,4,5,2,1]))