from tkinter import *
import pyautogui, sys, random, threading, sched, time
import pynput

volumeFlag = True  

def on_click(x, y, button, pressed):
    global volumeFlag;
    if pressed == True:
        volumeFlag = False

def volume():
    global volumeFlag
    if volumeFlag:  
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(5)

    root.after(1000, volume)

def start():
    global volumeFlag
    volumeFlag = True
    root.after(1000, volume)     

def stop():
    global volumeFlag
    volumeFlag = False


listener = pynput.mouse.Listener(
            on_click=on_click)

listener.start()

## Main ##
root = Tk()
root.title("Hi")
root.geometry("500x500")

app = Frame(root)
app.grid()

start = Button(app, text="Start...", command=start)

start.grid()
root.mainloop()


    
