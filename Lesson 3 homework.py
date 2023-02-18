# Calculator with 2 modes: lite and pro

# Creating a while loop not to end the program because of an error or typo
while True:
    # Asking user to choose the mode
    choose_mode = input('Please choose the mode of calculator: Lite or Pro.\n'
                        'Note, Lite only provides you with next operations:\n'
                        'addition +\ndivision /\nmultiplication *\nsubtraction -\n'
                        'You can type "q" to quit the program at any point.\n'
                        'Type: Lite or Pro for choosing respected mode: ')

# Lite mode calculator is activated
    if choose_mode == "lite" or choose_mode == "Lite":
        print("You've choose Lite mode.")

        # Creating a while loop not to end the program because of an error or typo
        while True:
            # Taking input from user with an option to quit the program
            try:
                lite_first_number = input("Using digits type your first number: ")
                if lite_first_number == "q" or lite_first_number == "Q":
                    quit()
                else:
                    lite_first_number = float(lite_first_number)

                lite_second_number = input("Now, I'm gonna need a second number: ")
                if lite_second_number == "q" or lite_second_number == "Q":
                    quit()
                else:
                    lite_second_number = float(lite_second_number)

                lite_operation = input("Using math sign tell me what you want to do with those numbers: ")
                if lite_operation == "q" or lite_operation == "Q":
                    quit()

                # Checking what operator was inputted and doing the calculation
                if lite_operation == '+':
                    print(lite_first_number + lite_second_number)
                    break
                elif lite_operation == '-':
                    print(lite_first_number - lite_second_number)
                    break
                elif lite_operation == "*":
                    print(lite_first_number * lite_second_number)
                    break
                elif lite_operation == '/':
                    print(lite_first_number / lite_second_number)
                    break
                else:
                    print('''Nah, in this mode you only can use 4 listed above operations.'''
                          ''' Don't forget that division uses "/"''')
                    continue
            except ValueError:
                print('Please only use digits and "." for decimals instead of ","')
                continue
        break

    # Pro mode calculator is activated
    elif choose_mode == "Pro" or choose_mode == "pro":
        print("You've choose Pro mode. You can do next operations with your numbers:\n"
              "+ addition\n/ division\n* multiplication\n- subtraction\n"
              "% modulo operation \n** ...to the power of... \n// division rounded down")

        # Creating a while loop not to end the program because of an error or typo
        while True:
            # Taking input from user with an option to quit the program
            try:
                pro_first_number = input("Using digits type your first number: ")
                if pro_first_number == "q" or pro_first_number == "Q":
                    quit()
                else:
                    pro_first_number = float(pro_first_number)

                pro_second_number = input("Now, I'm gonna need a second number: ")
                if pro_second_number == "q" or pro_second_number == "Q":
                    quit()
                else:
                    pro_second_number = float(pro_second_number)

                pro_operation = input("Using math sign tell me what you want to do with those numbers: ")
                if pro_operation == "q" or pro_operation == "Q":
                    quit()

                # Checking what operator was inputted and doing the calculation
                if pro_operation == '+':
                    print(pro_first_number + pro_second_number)
                    break
                elif pro_operation == '-':
                    print(pro_first_number - pro_second_number)
                    break
                elif pro_operation == "*":
                    print(pro_first_number * pro_second_number)
                    break
                elif pro_operation == '/':
                    print(pro_first_number / pro_second_number)
                    break
                elif pro_operation == '%':
                    print(pro_first_number % pro_second_number)
                    break
                elif pro_operation == '**':
                    print(pro_first_number ** pro_second_number)
                    break
                elif pro_operation == '//':
                    print(pro_first_number // pro_second_number)
                    break
                else:
                    print('''Nah, in this mode you can only use 7 listed above operations.'''
                          ''' Don't forget that division uses "/" and rounded down division - "//"''')
                    continue
            except ValueError:
                print('Please only use digits and "." for decimals instead of ","')
                continue
        break
    # User choose to quit the program or typed something else while choosing Lite or Pro mode
    elif choose_mode == "q" or choose_mode == "Q":
        quit()
    else:
        print('You had one job! Try again')
        continue