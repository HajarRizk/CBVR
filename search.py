import pickle

from cv2 import cv2

import histogram
import Searcher





with open("index.txt",'rb') as f:
    Dataset,Frames = pickle.load(f)



#extracting quary features and kframes
query_path = 'Queries/quary3.mp4'
query_features = histogram.HistogramGenerator(query_path)
query_histogram , query_kframes = query_features.generate_video_rgb_histogram()
query_features.destroy_video_capture()

for frame in query_kframes:
    frame1 = cv2.resize(frame, (300, 300))
    cv2.imshow('query_kframes',frame1)
    cv2.waitKey(0)




#performing the search Methods:
s1 = Searcher.Searcher('index.txt')
results = s1.search(query_histogram)


i=0
#loop over the results
for videoUID in results:
    #load the result videoUID and display it
    print(videoUID)
    i+=1
    for kframe in Frames[videoUID]:
        kframe1 = cv2.resize(kframe, (300, 300))
        cv2.imshow('video_'+str(i)+'_kframes', kframe1)
        cv2.waitKey(0)


