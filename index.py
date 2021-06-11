import pickle

import histogram

# Used for parsing command line arguments
import argparse
# Used for getting paths of our images
import glob

Dataset = {}
Frames = {}


# Using glob to get path of images and go through all of them
for videoPath in glob.glob("DataBase" + "/*.mp4"):
    # Get the UID of the image path and load the image
    videoUID = videoPath[videoPath.rfind("/") + 1:]
    video = histogram.HistogramGenerator(videoPath)

    # Using the describe function
    features,Kframes = video.generate_video_rgb_histogram()
    #write the features to Dataset Dictionary
    Dataset[videoUID] = features
    Frames[videoUID] = Kframes


    video.destroy_video_capture()
#Saving the dictionary to txt file
with open("index.txt",'wb') as f:
    pickle.dump([Dataset,Frames],f)





