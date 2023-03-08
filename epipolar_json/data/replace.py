# This file is used to replace empty dictionaries for some frames in the keypoints.json file with zeros for both "bbox" and "keypoints". 
#Please change the path when you are using
import json
import numpy as np


f = open('/Users/stlp/Desktop/sam/ram/pose/vis_results/yolox/S005/c028/keypoints.json', "r+")
file_data = json.load(f)

copy = file_data['annotations'].copy()

for idx,frame in enumerate(copy):
    if ('frame_id : '+str(idx)) not in file_data['annotations'][idx]:
        dict2 = {}
        dict2["bbox"] = np.zeros([5], dtype = float).tolist()
        dict2["keypoints"] = np.zeros([17,3], dtype = float).tolist()
        print(dict2)
        file_data['annotations'][idx]["frame_id : "+str(idx)] = [dict2]
        f.seek(0)
        
json.dump(file_data, f)
