#!/usr/bin/env python3

# todo & notes
# shift functionality does not currently work correctly
# implement home/end
# impelment backspace delete

# pip install keyboard
import keyboard

# BINDS: 

# block capslock key from changing capslock state:
keyboard.add_hotkey('capslock', lambda: empty(), suppress=True)

# CAPSLOCK:
keyboard.add_hotkey('capslock+a', lambda: keyboard.send('capslock'), suppress=True)

# ARROW KEYS
keyboard.add_hotkey('capslock+j', lambda: keyboard.send('left'), suppress=True)
keyboard.add_hotkey('capslock+k', lambda: keyboard.send('up'), suppress=True)
keyboard.add_hotkey('capslock+l', lambda: keyboard.send('down'), suppress=True)
keyboard.add_hotkey('capslock+;', lambda: keyboard.send('right'), suppress=True)
# ctrl+:
keyboard.add_hotkey('capslock+ctrl+j', lambda: keyboard.send('ctrl+left'), suppress=True)
keyboard.add_hotkey('capslock+ctrl+k', lambda: keyboard.send('ctrl+up'), suppress=True)
keyboard.add_hotkey('capslock+ctrl+l', lambda: keyboard.send('ctrl+down'), suppress=True)
keyboard.add_hotkey('capslock+ctrl+;', lambda: keyboard.send('ctrl+right'), suppress=True)
# right-alt as control:
keyboard.add_hotkey('capslock+right alt+j', lambda: keyboard.send('ctrl+left'), suppress=True)
keyboard.add_hotkey('capslock+right alt+k', lambda: keyboard.send('ctrl+up'), suppress=True)
keyboard.add_hotkey('capslock+right alt+l', lambda: keyboard.send('ctrl+down'), suppress=True)
keyboard.add_hotkey('capslock+right alt+;', lambda: keyboard.send('ctrl+right'), suppress=True)

# PAGE UP/DOWN
keyboard.add_hotkey('capslock+comma', lambda: keyboard.send('page up'), suppress=True)
keyboard.add_hotkey('capslock+.', lambda: keyboard.send('page down'), suppress=True)

# HOME/END KEYS
keyboard.add_hotkey('capslock+i', lambda: keyboard.send('home'), suppress=True)
keyboard.add_hotkey('capslock+o', lambda: keyboard.send('end'), suppress=True)
# ctrl+:
keyboard.add_hotkey('capslock+ctrl+i', lambda: keyboard.send('ctrl+home'), suppress=True)
keyboard.add_hotkey('capslock+ctrl+o', lambda: keyboard.send('ctrl+end'), suppress=True)
# right-alt as control:
keyboard.add_hotkey('capslock+right alt+i', lambda: keyboard.send('ctrl+home'), suppress=True)
keyboard.add_hotkey('capslock+right alt+o', lambda: keyboard.send('ctrl+end'), suppress=True)

# DELETE
keyboard.add_hotkey('capslock+backspace', lambda: keyboard.send('delete'), suppress=True)
# ctrl+:
keyboard.add_hotkey('capslock+ctrl+backspace', lambda: keyboard.send('ctrl+delete'), suppress=True)
# right-alt as control:
keyboard.add_hotkey('capslock+right alt+backspace', lambda: keyboard.send('ctrl+delete'), suppress=True)

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
