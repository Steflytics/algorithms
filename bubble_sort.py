def user_input():
    list_of_numbers = []
    new_number = True
    valid = False
    while new_number:
        try:
            number = int(input("Enter an integer "))
            list_of_numbers.append(number)
            valid = False
        except:
            continue
        while not valid:
            next_number = input("Another number to input? (y/n) ")
            if next_number == 'n':
                valid = True
                new_number = False
            if next_number == 'y':
                valid = True
    return list_of_numbers

# Define function for sorting
def bubble_sort(input_list):
    # set sorted variable to false
    sorted = False
    # while sorted = false go ahead
    while not sorted:
        # set sorted to true to end this while loop
        sorted = True
        # for every item in the list from 0 to length of list - 1
        for i in range(0, len(input_list)-1):
            # check if this item in list is bigger than the next item in the list
            if input_list[i] > input_list[i+1]:
                # if the current item is bigger than the next item then go ahead and set the sorted variable back to false
                sorted = False
                # swap the items in the list for example (2, 1) --> (1, 2)
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
    # return the bubble sorted list
    return input_list

print(bubble_sort(user_input()))