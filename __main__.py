#!/usr/bin/env python3

# todo & notes
# shift functionality does not work with arrow keys - maybe with pg u/d / home/end?
# implement all arrow and ctrl+arrow keys
# implement home/end & pg up/pg dwn
# impelment backspace delete

# pip install keyboard
import keyboard

# BINDS: 

# block capslock key from changing capslock state:
keyboard.add_hotkey('capslock', lambda: empty(), suppress=True)

# MAP CAPSLOCK:
keyboard.add_hotkey('capslock+a', lambda: keyboard.send('capslock'), suppress=True)

# MAP ARROW KEYS
# arrow keys:
keyboard.add_hotkey('capslock+j', lambda: keyboard.send('left'), suppress=True)
keyboard.add_hotkey('capslock+k', lambda: keyboard.send('up'), suppress=True)
keyboard.add_hotkey('capslock+l', lambda: keyboard.send('down'), suppress=True)
keyboard.add_hotkey('capslock+;', lambda: keyboard.send('right'), suppress=True)
# ctrl+arrow keys:
keyboard.add_hotkey('capslock+ctrl+j', lambda: keyboard.send('ctrl+left'), suppress=True)
keyboard.add_hotkey('capslock+ctrl+k', lambda: keyboard.send('ctrl+up'), suppress=True)
keyboard.add_hotkey('capslock+ctrl+l', lambda: keyboard.send('ctrl+down'), suppress=True)
keyboard.add_hotkey('capslock+ctrl+;', lambda: keyboard.send('ctrl+right'), suppress=True)

# MAP PAGE UP/DOWN
# pg up / pg dn:
# keyboard.add_hotkey('capslock+,', lambda: keyboard.send('page up'), suppress=True)
# keyboard.add_hotkey('capslock+.', lambda: keyboard.send('page down'), suppress=True)
# ctrl+ keys:
# keyboard.add_hotkey('capslock+ctrl+j', lambda: keyboard.send('ctrl+left'), suppress=True)
# keyboard.add_hotkey('capslock+ctrl+k', lambda: keyboard.send('ctrl+up'), suppress=True)

# SHIFT FUNCTIONALITY - On hold due to bug (Issue #330 on GitHub)
# keyboard.add_hotkey('capslock+ctrl+shift+j', lambda: keyboard.send('ctrl+shift+left'), suppress=True)
# keyboard.add_hotkey('capslock+ctrl+shift+;', lambda: keyboard.send('ctrl+shift+right'), suppress=True)
# keyboard.add_hotkey('ctrl+shift+x', lambda: keyboard.send('shift+left'), suppress=True)
# keyboard.add_hotkey('ctrl+shift+x', lambda: hold_shift(), suppress=True)
#
# def hold_shift():
#     keyboard.press('left')
#     keyboard.release('left')


# FUNCTIONS: 

# empty function used in blocking capslock key from changing capslock state
def empty():
    pass

def main():
    flag = 1
    while(flag): 
        pass

if __name__ == '__main__':
    main()
