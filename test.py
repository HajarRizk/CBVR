import pickle

import cv2

import histogram

def distance(histA, histB):
    # calculating the chi squared distance
    d = cv2.compareHist(histA, histB, cv2.HISTCMP_INTERSECT)
    # return the chi squared distance
    return d

with open("index.txt",'rb') as f:
    Dataset,Frames = pickle.load(f)



#print(len(Dataset))


frames = Frames['DataBase\\jellyfish.mp4']
for frame in frames:
    frame1 = cv2.resize(frame, (300, 300))
    cv2.imshow('frame',frame1)
    cv2.waitKey(0)
#test_video.destroy_video_capture()
dataset = Dataset['DataBase\\jellyfish.mp4']

query_path = 'DataBase\\jellyfish.mp4'
query_features = histogram.HistogramGenerator(query_path)
query_histogram , query_kframes = query_features.generate_video_rgb_histogram()
query_features.destroy_video_capture()

no_of_similar_frames = int(len(query_histogram) / 2 + 1)

similar_frames = 0
for kframe_quary in query_histogram: # loop over every kframes in quary
    count = 0
    for kframe_datasset in dataset: # loop over every kframe in testvideo
        d = distance(kframe_quary,kframe_datasset)
        print(d)
        if d>= 0.75:
            count+=1
    if (count >= 1):
        similar_frames += 1
    print(similar_frames)




# closing the reader
f.close()






