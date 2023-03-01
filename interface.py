### Standard library imports
import sys
import os

### Third party imports


### Local application imports

import tasks as tasks
import menu as menu



def clear_screen():
    """ Clear screen function """
    # posix is os name for Linux or Mac
    if (os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for Windows
    else:
        os.system('cls')


def exit_menu():
    """ Exit program function """
    print('')
    print('Good bye!')
    print('')
    sys.exit()


def get_menu_data(menu_number):
    """ Gets from specific menu data (using menu unique identifier)
        from the dictionary data structure """
    choosen_menu = menu.dict_menu[menu_number]
    return choosen_menu


def load_header_1(title, instruction):
    """ Load example format the layout 1 """
    print('')
    print(title)
    print('****************************')
    print(instruction)
    print('')


def load_header_2(title, instruction):
    """ Load example format the layout 2 """
    print('')
    print(title)
    print('============================')
    print(instruction)
    print('')


def load_header_3(title, instruction):
    """ Load example format the layout 3 """
    print('')
    print(title)
    print('----------------------------')
    print(instruction)
    print('')


def select_menu_header(retrived_menu: object) -> object:
    """ Uses menu data retrived from the dictionary.
    The format/layout function is selected using the format number.
    Retrived data (title and description) is passed into the relevant
    format function."""
    title = (retrived_menu['title'])
    description = (retrived_menu['instruction'])
    format = (retrived_menu['format'])
    if format == '1':
        load_header_1(title, description)
    elif format == '2':
        load_header_2(title, description)
    else:
        load_header_3(title, description)


def load_menu_list(retrived_menu):
    """ Uses retrieved data from the dictionary
    printing the key and value (description stored in
    element 0 in list)."""
    menu_values = (retrived_menu['table'])
    for keys, values in menu_values.items():
        print(keys, ':', values[0])
    print("")
    print('----------------------------')
    print("")
    return(menu_values)


def make_menu_choice(menu_table):
    """Uses while loop to check value entered by user is
       in dictionary (key). Passing the associated function name
       to the user input value to process"""
    while True:
        user_choice = str(input('What do you want to do: '))

        if user_choice in menu_table.keys():
            # Stores dictionary value (both elements)
            # in the variable
            function = menu_table.get(user_choice)

            # Calls the function using element 1 as
            # the argument
            return (user_choice, function[1])
        else:
            # If not in dictionary prints this and loops
            print('\nPlease try again...\n')


def load_task_choice(function_name, menu_number):
    """ Pass function name of task and previous menu number in using arguement """

    func_to_run = getattr(tasks, function_name)
    previous_menu = func_to_run(menu_number)
    return previous_menu


def display_menu(selected_menu_number):
    """ Loops through a process for generating the choosen menu
    displays and/or running selected task, unless the exit function is called. """
    while True:
        menu_data = get_menu_data(selected_menu_number)

        select_menu_header(menu_data)
        func_options = load_menu_list(menu_data)
        user_choice, function_name = make_menu_choice(func_options)

        if 'exit' in function_name:
            clear_screen()
            exit_menu()

        elif 'task' in function_name:
            clear_screen()
            prev_menu_number = load_task_choice(function_name, selected_menu_number)
            selected_menu_number = int(prev_menu_number)

        else:
            clear_screen()
            menu_opt_selected = any(char.isdigit() for char in function_name)
            if  menu_opt_selected == True:
                for char in function_name:
                    if char.isdigit():
                        menu_opt_number = char
                selected_menu_number = int(menu_opt_number)








