import pyautogui as pyautogui
from pynput.keyboard import Key, Listener
from threading import Thread
import tkinter as tk

check_close = 0

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.f20:
        return False
    if check_close:
        return False
    if key == Key.shift_l:
        pass

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////NEW

def otd():
    with Listener(on_release=on_release) as listener:
        listener.join()

exit_o = Thread(target=otd, args=())
exit_o.start()

def on_exit():
    global check_close
    check_close = 1
    pyautogui.press('f20')
    root.destroy()


try:
    root = tk.Tk()
except:
    check_close = 1
root.geometry('187x275-1-900')
root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
