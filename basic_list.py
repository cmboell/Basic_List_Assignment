"""
Assignment: Basic List Assignment
Program: basic_list.py
Author: Colby Boell
Last date modified: 02/25/2022

The purpose of this program is to prompt the user for input that (if a number or a float) will be added
to a list and printed out. If the user inputs a string or letter it will not be added to the list. This is done
by using functions and try statements.
"""


def make_list(num):
    # list variable
    a_list = []
    # for loop to add to list based on number passed through
    for i in range(num):
        # calls input function
        new_entry = get_input()
        # try statement for input validation
        try:
            float(new_entry)
            a_list.append(new_entry)
        except ValueError:
            # if not valid invalid message lets user know it won't be added to the list
            print('Invalid entry, entry not added to the list')
    # returns the list
    return a_list


# input function called in make_list function to validate and add to list
def get_input():
    # prompts user input and prints out the input they put in
    user_input = input("Enter a number: ")
    print(f'you entered {user_input}')
    return user_input


# main that calls make_list function
if __name__ == '__main__':
    # print statements calling make_list function passing number for number of times
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))

"""
Test output results:
1.)
Enter a number: 2
you entered 2
['2']
Enter a number: 1
you entered 1
Enter a number: 2
you entered 2
['1', '2']
Enter a number: 3
you entered 3
Enter a number: 2
you entered 2
Enter a number: 1
you entered 1
['3', '2', '1']
2.)
Enter a number: 3
you entered 3
['3']
Enter a number: 2
you entered 2
Enter a number: 1
you entered 1
['2', '1']
Enter a number: e
you entered e
Invalid entry, entry not added to the list
Enter a number: 5
you entered 5
Enter a number: 6
you entered 6
['5', '6']

"""
