import csv
import math
import os

import cv2
import imutils
import numpy as np


class HistogramGenerator:


    def __init__(self, path):
        """
        Initialise variables and create a VideoCapture object for a mp4 file.
        :param directory: the directory where the video file is located
        :param file_name: the mp4 video file's name
        """


        # start capturing video
        self.video_capture = cv2.VideoCapture(path)
        self.check_video_capture()



    def _normalise_histogram(self,frame):
        """
        Normalise a histogram using OpenCV's "normalize" function.
        :param hist: the histogram to normalise
        :return: the normalised histogram
        """
        bins = (16, 16, 16)
        hist = cv2.calcHist([frame], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
        if imutils.is_cv2():
            # For openCV version 2.4
            hist = cv2.normalize(hist).flatten()
        else:
            # For openCV version 3+
            hist = cv2.normalize(hist, hist).flatten()
        return hist




    def generate_video_rgb_histogram(self):
        """
        Generates multiple RGB histograms (one every second) for a video.
        :param is_query: boolean specifying if the input video is the query video (to select ROI)
        :param cur_ref_points: list of previously-used ROI point locations
        :return: None
        """
        # determine which frames to process for histograms
        frames = []
        frames_hist = []
        count = 0

        frame_counter = 0  # keep track of current frame ID to know to process it or not
        while self.video_capture.isOpened()  : #frame_counter<=10
            ret, frame = self.video_capture.read()  # read capture frame by frame
            if ret:
              hist = self._normalise_histogram(frame)
            count +=1
            if ret:
                if(len(frames_hist)==0):
                    frames.append(frame)
                    frames_hist.append(hist)

                else:
                    compare_method = cv2.HISTCMP_INTERSECT
                    diff = cv2.compareHist(hist, frames_hist[frame_counter-1], compare_method)
                    if diff <= 1:
                        frames.append(frame)
                        frames_hist.append(hist)

            else:
                break

        return frames_hist,frames



    def check_video_capture(self):
        """
        Checks if the VideoCapture object was correctly created.
        :return: None
        """
        if not self.video_capture.isOpened():
            print("Error opening video file")

    def destroy_video_capture(self):
        """
        Tidying up the OpenCV environment and the video capture.
        :return: None
        """
        self.video_capture.release()
        cv2.destroyAllWindows()






#test_video = HistogramGenerator('DataBase/scene-segmentation.mp4')
#hist , frames = test_video.generate_video_rgb_histogram()
#for frame in frames:
#    frame1 = cv2.resize(frame, (300, 300))
#    cv2.imshow('frame',frame1)
#    cv2.waitKey(0)
#test_video.destroy_video_capture()





