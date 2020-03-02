#!/usr/bin/env python3

# pip install keyboard
import keyboard

# block capslock key from changing capslock state:
keyboard.add_hotkey('capslock', lambda: print('should not enable capslock'), suppress=True)

# map caps+a to capslock:
keyboard.add_hotkey('capslock+a', lambda: keyboard.send('capslock'), suppress=True)

# map caps+j to left arrow:
keyboard.add_hotkey('capslock+j', lambda: keyboard.send('left'), suppress=True)
keyboard.add_hotkey('capslock+ctrl+j', lambda: keyboard.send('ctrl+left'), suppress=True)
keyboard.add_hotkey('capslock+ctrl+shift+j', lambda: hold_shift(), suppress=True)
# to implement ctrl+shift+left: create hook(?) 
# while keys are pressed, shift key_down
# if j then send left
# if keys are not pressed, shift key_up
# # keyboard.add_hotkey('capslock+ctrl+shift+j', lambda: keyboard.send('ctrl+shift+left'), suppress=True)

print(__name__)

def hold_shift():
    while(keyboard.is_pressed('shift')):
        keyboard.press('shift')
        if keyboard.is_pressed('j'):
            keyboard.send('ctrl+left')
        keyboard.release('shift')

def main():
    flag = 1
    while(flag): 
        print(flag)

if __name__ == '__main__':
    main()


