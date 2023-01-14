from pynput import keyboard, mouse
from time import sleep

keyboard_ctrl = keyboard.Controller()
mouse_ctrl = mouse.Controller()


# moves the mouse to click on a coordinate, (0, 0) is on top left
def click(x, y):
    mouse_ctrl.move(-1600, -900)
    mouse_ctrl.move(x, y)
    sleep(0.1)
    mouse_ctrl.click(mouse.Button.left)
    sleep(0.1)


# presses ctrl and a letter
def ctrl(letter):
    keyboard_ctrl.press(keyboard.Key.ctrl)
    keyboard_ctrl.type(letter)
    sleep(0.1)
    keyboard_ctrl.release(keyboard.Key.ctrl)
    sleep(0.1)


# the most privileged action a teenager boy can act out
def altab():
    keyboard_ctrl.press(keyboard.Key.alt)
    keyboard_ctrl.press(keyboard.Key.tab)
    sleep(0.1)
    keyboard_ctrl.release(keyboard.Key.tab)
    keyboard_ctrl.release(keyboard.Key.alt)
    sleep(0.2)


# checks for her comment
def who(name, yes='yes'):
    comments = open('comments.txt', 'r+', encoding='utf-8').readlines()
    for i in range(len(comments) - 3):
        if comments[i] == name + '\n' \
                and not comments[i + 1][: 9] == 'Yesterday' \
                and not comments[i + 1][2] == '/' \
                and (comments[i + 2][: 3] == yes.title()
                     or comments[i + 2][: 3] == yes):
            return True

    return False


# just opens stuff - the coordinates are for the chat/thing to click
def open_shit(x1, y1, x2, y2):
    # closing pycharm
    click(1420, 15)

    # Type here to search
    click(100, 845)
    sleep(3)
    keyboard_ctrl.type('comments.txt')
    sleep(1.5)
    keyboard_ctrl.type('\n')
    sleep(4)

    # type some shit
    ctrl('a')
    keyboard_ctrl.type('lierally nothing, i just want to delete some shit')

    # open thing tab
    click(x1, y1)

    # click generally on ______
    click(x2, y2)

    # just wait a bit for the first
    sleep(6)


def main():
    # opening shit with comments
    open_shit(1100, 70, 1370, 715)

    # wait for message
    while True:
        # emergency
        if mouse_ctrl.position[0] > 1400:
            quit()

        # copies everything
        click(1370, 715)
        ctrl('a')
        ctrl('c')
        altab()

        # puts it into file
        ctrl('a')
        ctrl('v')
        ctrl('s')
        altab()

        # Tom Taylor and Elena Tohux for Spanish
        if who('Emily Twyning') or who('Alex Tubbs'):
            break

    # Type a new message
    click(1375, 760)
    keyboard_ctrl.type('yes\n')

    # Leave
    click(1460, 75)

    # close comments.txt
    sleep(3)
    ctrl('w')


if __name__ == "__main__":
    main()

