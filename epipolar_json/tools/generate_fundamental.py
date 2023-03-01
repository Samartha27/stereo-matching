import json
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import argparse
import os
from os.path import basename, splitext
import utils
import sys
sys.path.append('/Users/stlp/Desktop/sam/ram/pose/epipolar_json/')
from data import datasets



  
def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--r_img", help="Input the right image directory", required=True)
    parser.add_argument("--l_img", help="Input the left image directory",  required=True)
    parser.add_argument("--l_keypoints", help="Input only the session and camera directories of left keypoints",  required=True)
    parser.add_argument("--r_keypoints", help="Input only the session and camera directories of right keypoints",  required=True)
    parser.add_argument("--frames", nargs='+', help="Input the right image directory", required=True)

    args = parser.parse_args()

    output_file = splitext(basename(args.l_img))[0] +"_"+ splitext(basename(args.r_img))[0]
    
    im1 = io.imread(args.l_img)
    im2 = io.imread(args.r_img)
    
    points1 = datasets.generate_points(args.l_keypoints, args.frames)
    points2 = datasets.generate_points(args.r_keypoints, args.frames)
    
    print(points1.shape)
    print(points2.shape)
    assert (points1.shape == points2.shape)

    F = utils.compute_fundamental_matrix_normalized(points1, points2, output_file)

    p1 = points1.T[:, 0]
    p2 = points2.T[:, 0]

    assert(np.round(p2.T @ F @ p1)==0), "The constraint equation for the Fundamental matrix does not hold true"

    utils.plot_epipolar_lines(im1, im2, points1, points2, output_file)


if __name__ == "__main__":
    main()