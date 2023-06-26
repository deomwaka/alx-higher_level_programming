def safe_print_list(my_list=[], x=0):
    count = 0  # Counter to keep track of printed elements

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Ignore index errors when x is greater than the length of my_list

    print()  # Print a new line after all elements
    return count
