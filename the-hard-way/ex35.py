from sys import exit
from re import sub

# TODO: Refactor with dictionaries
GOLD_THRESHOLD = 50

ROOM_BEAR = 'bear'
ROOM_GOLD = 'gold'
ROOM_START = 'start'
ROOM_CTHULHU = 'chulhu'

ACTION_LEFT = 'left'
ACTION_RIGHT = 'right'
ACTION_TAKE_HONEY = 'take honey'
ACTION_TAUNT_BEAR = 'taunt bear'
ACTION_OPEN_DOOR = 'open door'
ACTION_FLEE = 'flee'
ACTION_HEAD = 'head'


def dead(why):
    print(why, 'Good job!')
    exit(0)

def print_text_block(text):
    """
    Trims the text, substitutes any excessive whitespace with one
    and prints it
    """
    text_block = text.strip()
    text_block = sub('\n[ ]+', '\n', text_block)
    print(text_block)

def show_available_actions(room):
    print('<::::::::::::::::::::::::::}]xxxx()o')
    if room == ROOM_BEAR:
        print(ACTION_TAKE_HONEY)
        print(ACTION_TAUNT_BEAR)
        print(ACTION_OPEN_DOOR)
    elif room == ROOM_START:
        print(ACTION_LEFT)
        print(ACTION_RIGHT)
    elif room == ROOM_CTHULHU:
        print(ACTION_FLEE)
        print(ACTION_HEAD)
    print('<::::::::::::::::::::::::::}]xxxx()o')


def gold_room():
    print_text_block(
        """
        This room is full of gold. How much do you take?
        """
    )

    choice = input('> ')
    if choice.isnumeric():
        how_much = int(choice)
    else:
        dead('Man, learn to type a number.')

    if how_much < GOLD_THRESHOLD:
        print('Nice, you\'re not greedy, you win!')
        exit(0)
    else:
        dead('You greedy bastard!')


def bear_room():
    print_text_block(
        """
        There is a bear here.
        The bear has a bunch of honey.
        The fat bear is in front of another door.
        How are you going to move the bear?
        """
    )

    show_available_actions(ROOM_BEAR)
    bear_moved = False

    while True:
        choice = input('> ')

        if choice == ACTION_TAKE_HONEY:
            dead('The bear looks at you then slaps your face off.')
        elif choice == ACTION_TAUNT_BEAR and not bear_moved:
            print('The bear has moved from the door.')
            print('You can go through it now.')
            bear_moved = True
        elif choice == ACTION_TAUNT_BEAR and bear_moved:
            dead('The bear gets pissed off and chews your leg off.')
        elif choice == ACTION_OPEN_DOOR and bear_moved:
            gold_room()
        else:
            print('I got no idea what that means.')
            show_available_actions(ROOM_BEAR)


def cthulhu_room():
    print_text_block(
        """
        Here you see the great evil Cthulhu.
        He, it, whatever stares at you and you go insane.
        Do you flee for your life or eat your head?
        """
    )
    show_available_actions(ROOM_CTHULHU)

    choice = input('> ')

    if choice == ACTION_FLEE:
        start()
    elif choice == ACTION_HEAD:
        dead('Well that was tasty!')
    else:
        cthulhu_room()


def start():
    print_text_block(
        """
        You are in a dark room.
        There is a door to your right and left.
        Which one do you take?
        """
    )
    show_available_actions(ROOM_START)

    choice = input('> ')

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else:
        dead('You stumble around the room until you starve.')


start()
