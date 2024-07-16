a_list =[4,1,5,3,2]
def selectionsort(unsorted_list):
    print(unsorted_list)
    for i in range(len(unsorted_list)):
        smaller_index = i
        for j in range (i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[smaller_index]:
                smaller_index = j
    unsorted_list[smaller_index], unsorted_list[i] = unsorted_list[i], unsorted_list[smaller_index]
    print(unsorted_list)
selectionsort(a_list)

# THE SECON
a_list = [1,2,3,4,5,6,7,8,9,10]
def binarysearch(list,value):
    left_edge, right_edge = 0, len(list)-1
    while left_edge <= right_edge:
        middle = left_edge + (right_edge -1)//2
        if list[middle] == value:
            return middle
        elif list[middle] < value:
            left_edge = middle + 1
        else:
            right_edge = middle - 1
            return -1
        print(binarysearch(a_list, 5))