import numpy as np
import cv2
from skimage import io
import load_camera_parameters
import utils
import argparse
import matplotlib.pyplot as plt
from os.path import basename, splitext

"""
intrinsic_left,extrinsic_left = load_camera_parameters.left("./testing/left.json")
intrinsic_right,extrinsic_right = load_camera_parameters.right("./testing/right.json")
"""

def main():
    

    parser = argparse.ArgumentParser()
    parser.add_argument("--r_img", help="Input the right image directory", required=True)
    parser.add_argument("--l_img", help="Input the left image directory",  required=True)
    args = parser.parse_args()

    output_file = splitext(basename(args.l_img))[0] +"_"+ splitext(basename(args.r_img))[0]
    
    im1 = io.imread(args.l_img)
    im2 = io.imread(args.r_img)

    points1 = np.load("./data/"+ splitext(basename(args.l_img))[0]+".npy")
    points2 = np.load("./data/"+ splitext(basename(args.r_img))[0]+".npy")
    

    assert (points1.shape == points2.shape)

    F = utils.compute_fundamental_matrix_normalized(points1, points2,output_file)

    p1 = points1.T[:, 0]
    p2 = points2.T[:, 0]

    assert(np.round(p2.T @ F @ p1)==0), "The constraint equation does not match"

    utils.plot_epipolar_lines(im1, im2, points1, points2, output_file)



if __name__ == "__main__":
    main()