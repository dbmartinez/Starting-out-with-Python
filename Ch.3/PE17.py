# Wi-Fi Diagnostic Tree

print('Reboot the computer and try to connect.')

user_input = input('Did that fix the problem?: ')

if user_input == 'no':
    print('\nReboot the router and try to connect.')
    user_input = input('Did that fix the problem?: ')

    if user_input == 'no':
        print('\nMake sure the cables between the router & modem are plugged in firmly.')
        user_input = input('Did that fix the problem?: ')

        if user_input == 'no':
            print('\nMove the router to a new location and try to connect.')
            user_input = input('Did that fix the problem?: ')

            if user_input == 'no':
                print('\nGet a new router.')