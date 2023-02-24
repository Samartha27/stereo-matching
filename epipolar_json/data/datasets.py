import json
import numpy as np
import os
import matplotlib.pyplot as plt

def generate_points(folder, frames):

    f = open(os.path.join('/Users/stlp/Desktop/sam/ram/pose/vis_results',str(folder),'keypoints.json'))
    keypoints = json.load(f)
    
    arrays = list()
    for frame_id in frames:
        frame_id = int(frame_id)

        for idx,val in enumerate(keypoints['annotations'][frame_id]['frame_id : '+str(frame_id)]):
            if idx == 2:  # Change this value to control how many humans you want in a frame. They might not be available in both the frames
                break
            arrays.append(np.array(keypoints['annotations'][frame_id]['frame_id : '+str(frame_id)][idx]["keypoints"]))
            
        

    array = np.vstack(arrays)
    for i in range(array.shape[0]):
        array[i][2] = 1

    #Save data
    np.save('./data/'+str(folder)+'.npy',array)
    f.close()

    return array