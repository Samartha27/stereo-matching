import argparse
import numpy as np
import matplotlib.pyplot as plt
import os
from os.path import basename, splitext
import sys
sys.path.append('/Users/stlp/Desktop/sam/ram/pose/epipolar_json/')
from data import datasets
from skimage import io
import utils




def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--r_img", help="Input the right image directory", required=True)
    parser.add_argument("--l_img", help="Input the left image directory",  required=True)
    parser.add_argument("--l_keypoints", help="Input only the session and camera directories of left keypoints",  required=True)
    parser.add_argument("--r_keypoints", help="Input only the session and camera directories of right keypoints",  required=True)
    parser.add_argument("--limit", help="Input the limit to number of person detections", required=True)
    parser.add_argument("--frames", nargs='+', help="Input the right image directory", required=True)
    parser.add_argument("--fm", help="Input the path to fundamental",  required=True)

    args = parser.parse_args()

    output_file = 'FM_' + splitext(basename(args.l_img))[0] +"_"+ splitext(basename(args.r_img))[0]
    
    im1 = io.imread(args.l_img)
    im2 = io.imread(args.r_img)
    
    points1 = datasets.generate_points(args.l_keypoints, args.frames, args.limit)
    points2 = datasets.generate_points(args.r_keypoints, args.frames, args.limit)
    
    print(points1.shape)
    print(points2.shape)
    assert (points1.shape == points2.shape)

    F = np.load(args.fm)
    print("Fundamental matrix : \n",F)

    p1 = points1.T[:, 0]
    p2 = points2.T[:, 0]

    assert(np.round(p2.T @ F @ p1)==0), "The constraint equation for the Fundamental matrix does not hold true"

    utils.draw_epipolar_lines(im1, im2, points1, points2, output_file, F)


if __name__ == "__main__":
    main()


