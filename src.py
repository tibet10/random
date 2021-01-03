from tkinter import *
import pyautogui, sys, random, threading, sched, time
import pynput

isMoving = True  

def on_click(x, y, button, pressed):
    global isMoving;
    if pressed == True:
        isMoving = False

def moveMouse():
    global isMoving
    if isMoving:  
        pyautogui.moveTo(random.randint(1,1000), random.randint(1,1000), 2, pyautogui.easeInQuad)

    root.after(1000, moveMouse)

def start():
    global isMoving
    isMoving = True

def stop():
    global isMoving
    isMoving = False


## Main ##
listener = pynput.mouse.Listener(
            on_click=on_click)

listener.start()

root = Tk()
root.title("Title")
root.geometry("500x500")

app = Frame(root)
app.grid()

start = Button(app, text="Start mouse move...", command=start)

start.grid()

root.after(1000, moveMouse)  
root.mainloop()


    
