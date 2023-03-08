#Refer README file for sample command to run this file.

import argparse
import numpy as np
import matplotlib.pyplot as plt
from os.path import basename, splitext, dirname, join
import sys
sys.path.append('/Users/stlp/Desktop/sam/ram/pose/epipolar_json/')
from data import datasets
from skimage import io
import utils
import json


def preprocess_points(array):

    array = np.array(array)
    for i in range(array.shape[0]):
        array[i][2] = 1
    
    return array



def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--original_camera", help="Input only the camera number in original representation ex:c076",  required=True)
    parser.add_argument("--original_keypoints", help="Input path to original keypoints",  required=True)
    parser.add_argument("--neighbor_keypoints", nargs='+', help="Input path/paths to neighbor keypoints", required=True)
    parser.add_argument("--fm", help="Input the path to FM table",  required=True)
    args = parser.parse_args()


    

    f1 = open(args.original_keypoints, "r")
    original = json.load(f1)


    epipolar_distances = dict()
    frames = []

    for idx,frame in enumerate(original['annotations']):
        people_in_frame = dict()

        print(idx)
        for idx2,people in enumerate(frame['frame_id : '+str(idx)]):

            neighbor_dict = dict()
            for neighbor_kpts in args.neighbor_keypoints:
                f2 = open(neighbor_kpts, "r")
                neighbor = json.load(f2)

                distances_nb = list()
                for idx_nb,people_nb in enumerate(neighbor['annotations'][idx]['frame_id : '+str(idx)]):
                    
                    # Load fundamental matrix
                    fm = open(args.fm, "r")
                    for row in fm:
                        cameras = row.split()
                        if basename(dirname(args.original_keypoints)) in cameras:
                            if basename(dirname(neighbor_kpts)) in cameras:
                                F = np.load(cameras[2])
                    fm.close()

                    
                    distances = utils.distances_epipolar_lines(preprocess_points(people["keypoints"]), 
                                                        preprocess_points(people_nb["keypoints"]),
                                                        F)
                    distances_nb.append(distances)
                
                neighbor_dict[basename(dirname(neighbor_kpts))] = distances_nb
                f2.close()

            people_in_frame[idx2] = neighbor_dict
                
        frames.append(people_in_frame)
        
        
        # if idx == 2: # Use this to run only on first n frames
        #     break
    
    f1.close()


    epipolar_distances["distances"] = frames


    print("Writing to json file.....")
    


    json_object = json.dumps(epipolar_distances, indent = 2)

    output_file = join('./output/distances/', 'Dist_'+args.original_camera+".json")
    with open(output_file, "w") as outfile:
        outfile.write(json_object)
        print("Done")


if __name__ == "__main__":
    main()

