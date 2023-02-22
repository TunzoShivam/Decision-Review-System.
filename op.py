import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
from functools import partial
import time
import threading
import imutils

stream = cv2.VideoCapture("clip2.mp4")
stream2 = cv2.VideoCapture("clip1.mp4")
flag = True


def catch_out(speed2):
    global flag
    print(f"You clicked on play. Speed is {speed2}")

    # Play the video in reverse and forward mode
    frame2 = stream2.get(cv2.CAP_PROP_POS_FRAMES)
    stream2.set(cv2.CAP_PROP_POS_FRAMES, frame2 + speed2)

    grabbed, frame = stream2.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black",
                           font="Times 26 bold", text="Decision Pending")
    flag = not flag


def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black",
                           font="Times 26 bold", text="Decision Pending")
    flag = not flag


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()


def notout():
    thread = threading.Thread(target=pending, args=("notout",))
    thread.daemon = 1
    thread.start()


def pending(decision):
    # 1.decision pending
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 2.wait
    time.sleep(4)
    # 3.out/notout
    if decision == 'out':
        frame = cv2.cvtColor(cv2.imread("out.png"), cv2.COLOR_BGR2RGB)
    if decision == 'notout':
        frame = cv2.cvtColor(cv2.imread("not_out.png"), cv2.COLOR_BGR2RGB)

    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4.wait
    time.sleep(3)
    # 5.credit
    frame = cv2.cvtColor(cv2.imread("credit.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


# width and height
SET_WIDTH = 1250
SET_HEIGHT = 630

# tkinter gui
window = tkinter.Tk()
window.title("DRS SYSTEM USING PYTHON BY KUNAL AND SHIVAM")
img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# Buttons
btn = tkinter.Button(window, text="<<previous (RUN Out)",
                     width=50, command=partial(play, -1.5))
btn.pack()
btn = tkinter.Button(window, text="next >> (RUN Out)",
                     width=50, command=partial(play, 3))
btn.pack()
btn = tkinter.Button(window, text="<<previous (Stump Out)",
                     width=50, command=partial(catch_out, -3))
btn.pack()
btn = tkinter.Button(window, text="next >> (Stump Out)",
                     width=50, command=partial(catch_out, 3))
btn.pack()
btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()
btn = tkinter.Button(window, text="Give Notout", width=50, command=notout)
btn.pack()
window.mainloop()
