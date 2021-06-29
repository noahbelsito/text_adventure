from rooms import *


def start():
    print("You wake up alone in a dark room.")
    print("You must find your way through the darkness.")
    print("Press 'o' to search for the lights or 'd' to search for doors")
    user_input = take_input().lower()
    if user_input == 'o':
        print("You now see two doors. Once you pass through a door you can't come back")
        print("Left or Right door? (l or r)")
        user_input = take_input().lower()
        if user_input == 'l':
            room_1()
        elif user_input == 'r':
            room_2()
        else:
            the_end('Not an option. The end.')
    elif user_input == 'd':
        print("You look for doors but step on a mine. You died.")
    else:
        the_end('Not an option. The end')


start()
