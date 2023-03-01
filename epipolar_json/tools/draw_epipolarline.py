import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import argparse
from os.path import basename, splitext
import utils


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", help="Input the right image directory", required=True)
    parser.add_argument("-l", help="Input the left image directory",  required=True)
    parser.add_argument("-lk", help="Input only the session and camera directories of left keypoints",  required=True)
    parser.add_argument("-F", required=True)

    args = parser.parse_args()
    
    im1 = io.imread(args.l)
    im2 = io.imread(args.r)
    
    points1 = np.load(args.lk)


    F = np.load(args.F)

    utils.draw_epipolar_lines(im1, im2, points1, F)


if __name__ == "__main__":
    main()