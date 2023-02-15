import numpy as np
import cv2
from skimage import io
from skimage.color import rgb2gray
import load_camera_parameters
import utils


intrinsic_left,extrinsic_left = load_camera_parameters.left("left.json")
intrinsic_right,extrinsic_right = load_camera_parameters.right("right.json")


im1 = io.imread("./data/right.png")
im2 = io.imread("./data/left.png")



points1 = np.load("right.npy")
points2 = np.load("left.npy")

assert (points1.shape == points2.shape)

F = utils.compute_fundamental_matrix_normalized(points1, points2)

p1 = points1.T[:, 0]
p2 = points2.T[:, 0]

print("The constraint eauation holds",np.round(p2.T @ F @ p1)==0)

utils.plot_epipolar_lines(im1, im2, points1, points2)