import pickle

from cv2 import cv2
import cv2
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd
import os
from pathlib import Path
import PIL.Image, PIL.ImageTk
import histogram
import Searcher


def clicked2():
    global filename
    filename = askopenfilename()
    print(filename)


def clicked():
    with open("index.txt", 'rb') as f:
        Dataset, Frames = pickle.load(f)

    # extracting quary features and kframes
    query_path = filename  # path taken from the user
    query_features = histogram.HistogramGenerator(query_path)
    query_histogram, query_kframes = query_features.generate_video_rgb_histogram()
    query_features.destroy_video_capture()

    for frame in query_kframes:
        frame1 = cv2.resize(frame, (300, 300))
        cv2.imshow('query_kframes', frame1)
        cv2.waitKey(0)

    # performing the search Methods:
    s1 = Searcher.Searcher('index.txt')
    results = s1.search(query_histogram)

    i = 0
    # loop over the results
    for videoUID in results:
        # load the result videoUID and display it
        print(videoUID)
        i += 1
        for kframe in Frames[videoUID]:
            kframe1 = cv2.resize(kframe, (300, 300))
            cv2.imshow('video_' + str(i) + '_kframes', kframe1)
            cv2.waitKey(0)


window = Tk()
window.title("Content Based Multimedia Retrieval System")
window.geometry('300x200')

lbl = Label(window, text="Hello")

btn = Button(window, text="Search", bg="black", fg="white", command=clicked, padx=50)
btn2 = Button(window, text="Choose query video", bg="black", fg="white", command=clicked2)

btn.grid(column=0, row=3)
btn2.grid(column=0, row=2)
lbl.grid(column=0, row=0)

window.mainloop()
