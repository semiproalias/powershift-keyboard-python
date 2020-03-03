#!/usr/bin/env python3

# NOTE: shift and alt functionality do not currently work correctly in Windows 10 due to noted lib issues

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

# OMMITTED DUE TO KEYBOARD LIBRARY ISSUE 332 - Alt+Arrow Issue
# alt+ (left-alt):
# keyboard.add_hotkey('capslock+left alt+j', lambda: keyboard.send('left alt+left'), suppress=True)
# keyboard.add_hotkey('capslock+left alt+k', lambda: keyboard.send('left alt+up'), suppress=True)
# keyboard.add_hotkey('capslock+left alt+l', lambda: keyboard.send('left alt+down'), suppress=True)
# keyboard.add_hotkey('capslock+left alt+;', lambda: keyboard.send('left alt+right'), suppress=True)

# OMMITTED UNTIL KEYBOARD LIBRARY SHIFT FUNCTIONALITY (ISSUE 330) IS RESOLVED
# # alt+shift+ (left-alt):
# keyboard.add_hotkey('capslock+left alt+shift+j', lambda: keyboard.send('left alt+shift+left'), suppress=True)
# keyboard.add_hotkey('capslock+left alt+shift+k', lambda: keyboard.send('left alt+shift+up'), suppress=True)
# keyboard.add_hotkey('capslock+left alt+shift+l', lambda: keyboard.send('left alt+shift+down'), suppress=True)
# keyboard.add_hotkey('capslock+left alt+shift+;', lambda: keyboard.send('left alt+shift+right'), suppress=True)

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
# keyboard.add_hotkey('ctrl+shift+x', lambda: fn_test(), suppress=True)
#
# def fn_test():
#     keyboard.press('alt')
#     keyboard.press('down')
#     keyboard.release('down')
#     keyboard.release('alt')

# FUNCTIONS: 

# empty function used in blocking capslock key from changing capslock state
def empty():
    pass

# superfluous loop used for testing in the debugger:
def main():
    flag = 1
    while(flag): 
        pass

# super flu as well; for testing purposes:
if __name__ == '__main__':
    main()
