def selection_sort(list_a):

    for i in range(0,len(list_a)-1):
        # default value
        min_value = i

        for j in range(i+1, len(list_a)):
            # if the right value is smaller than the left value then swap the numbers
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a

print(selection_sort([3,4,1,2,5]))
