import sys
import os
from collections import defaultdict
import numpy as np
import cv2

def dataset(base_dir) :
    d = defaultdict(list)
    
    for root, dirs, files in os.walk(base_dir) :
        for filename in files :
            file_path = os.path.join(root, filename)
            assert file_path.startswith(base_dir)
            suffix = file_path[len(base_dir):]
            suffix = suffix.lstrip("\\")
            label = suffix.split("\\")[0]
            if label is "1" or label is "0":
                d[label].append(file_path)

    tags = sorted(d.keys())
    #print("classes : {}".format(tags))
    #print(d[".DS_Store"])

    X = []
    y = []
    
    for class_index, class_name in enumerate(tags) :
        filenames = d[class_name]
        for filename in filenames :
            img = cv2.imread(filename)
            if img is not None :
                height, width, chan = img.shape

                assert chan == 3

                X.append(img)
                y.append(class_index)

    X = np.array(X).astype(np.float32)
    y = np.array(y)
        
    #print("X : {}\ny : {}\ntags : {}\n".format(X,y,tags))

    return X, y, tags

#dataset("{}/dataset/dataset_BTC_100_50/test".format(os.getcwd()))
