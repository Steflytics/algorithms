# Define function for user input
def user_input():
    # Create empty list
    list_of_numbers = []
    # Initialize variables for While loop
    new_number = True
    valid = True
    # While user wants new number
    while new_number:
        # Use try to catch potential false user input like non integer values
        try:
            # convert input which is a string to integer
            number = int(input("Enter an integer "))
            # add the integer to list
            list_of_numbers.append(number)
            # set variable valid to true fot next valid iteration
            valid = True
        # exception if try returns an error
        except:
            # skipt next steps
            continue
        while valid:
            # ask user for another integer
            next_number = input("Another number to input? (y/n) ")
            if next_number == 'n':
                valid = False
                new_number = False
            if next_number == 'y':
                valid = False
    # return the list
    return list_of_numbers

# Define function for sorting
def bubble_sort():
    input_list = user_input()
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

print(bubble_sort())