import pickle

import numpy as np
import csv

from cv2 import cv2


class Searcher:
    def __init__(self, indexPath):
        # storing the index
        self.indexPath = indexPath

    def search(self, queryFeatures):
        # make a list for thr results
        results = []

        # open the index file for reading
        with open(self.indexPath, 'rb') as f:
            Dataset, Frames = pickle.load(f)

            no_of_similar_frames = int(len(queryFeatures) / 2 + 1)
            for (videoID,features) in Dataset.items(): #loop over every video in dataset
                similar_frames = 0
                for kframe_quary in queryFeatures : # loop over every kframes in quary
                    count = 0
                    for kframe_datasset in features: # loop over every kframe in testvideo
                        d = self.distance(kframe_quary,kframe_datasset)
                        if d>= 2:
                            count+=1
                    if (count >= 1):
                        similar_frames += 1
                    if (similar_frames >= no_of_similar_frames):
                        results.append(videoID)
                        break



            # closing the reader
            f.close()



        # return our results
        return results

    def distance(self, histA, histB):
        # calculating the chi squared distance
        d = cv2.compareHist(histA, histB, cv2.HISTCMP_INTERSECT)
        # return the chi squared distance
        return d




