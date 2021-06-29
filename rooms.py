from utils import *


def room_1():
    items = ['key_1', 'key_2', 'key_3', 'key_4', 'key_5', 'key_6']
    print('You walk into a room with 6 keys. Only two of the keys will open doors and you have two doors.')
    print('You only have 3 chances.')

    tries = 0
    while tries < 3:
        print('Which key do you pick? (1 - 6)')
        try:
            user_input = int(take_input())
        except ValueError:
            the_end("That isn't even a number? You dumb or something?")
            break
        if user_input == 1:
            print('This key opens neither door.')
            tries += 1
        elif user_input == 2:
            print('This key opens the second door. Do you want to enter? (y or n)')
            user_input = take_input().lower()
            if user_input == 'y':
                the_end('You befriend a gorilla that destroys the wall behind him and lets you free of this game.')
                break
            elif user_input == 'n':
                tries += 1
                continue
            else:
                the_end('Not an option.')
                break
        elif user_input == 3:
            print('This key opens neither door.')
            tries += 1
        elif user_input == 4:
            print('This key opens neither door.')
            tries += 1
        elif user_input == 5:
            print('This opens the first door. Do you want to enter? (y or n)')
            if take_input().lower() == 'y':
                the_end('You take a flight to mars. Where you will have to learn to live for the rest of your life...')
                break
            elif take_input().lower() == 'n':
                tries += 1
                continue
            else:
                the_end('Not an option.')
                break
        elif user_input == 6:
            print('This key opens neither door.')
            tries += 1
        else:
            the_end('Not an option.')
            break
    if tries == 3:
        the_end('You run out of tries and the room explodes.')
    else:
        the_end('The end.')


def room_2():
    print('Hi')
