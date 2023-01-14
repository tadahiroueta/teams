from pynput import keyboard, mouse
from time import sleep
from presente import click, ctrl, altab, open_shit

keyboard_ctrl = keyboard.Controller()
mouse_ctrl = mouse.Controller()


# checks for a lot of people leaving the call
def people_quitting():
    comments = open('comments.txt', 'r+', encoding='utf-8').readlines()
    # find line which gives the number of people
    for line in comments:
        if line[: 9] == 'Attendees':
            # gets the number of people
            number = int(line[11: -2])
            if number <= 10:
                return True

    return False


def main():
    # open people tab
    open_shit(1050, 70, 1310, 230)

    # wait for message
    while True:
        # emergency
        if mouse_ctrl.position[0] > 1400:
            quit()

        # copies everything
        click(1310, 230)
        ctrl('a')
        ctrl('c')
        altab()

        # puts it into file
        ctrl('a')
        ctrl('v')
        ctrl('s')
        altab()

        if people_quitting():
            break

    # Leave
    click(1460, 75)

    # close comments.txt
    sleep(3)
    ctrl('w')


main()
