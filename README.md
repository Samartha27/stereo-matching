# stereo-matching

## Implementation

Generate points

`python data/generate_points.py`

Generate plot

`python tools/epipolar_geometry.py --r_img ./data/right.jpg --l_img ./data/left.jpg`



For Epiploar_json directory, only run:
 `python tools/generate_fundamental.py  --l_img /Users/stlp/Desktop/sam/ram/pose/test/S014/c078/c078.jpg --r_img /Users/stlp/Desktop/sam/ram/pose/test/S014/c076/c076.jpg --l_keypoints c078 --r_keypoints c076 --frames 9250`

## Sample output:
Fundamental matrix : \
 [[ 9.93947782e-07 -4.48011207e-05  1.63459154e-02] \
 [ 3.93890229e-05 -4.98987293e-06  2.40110466e-03] \
 [-1.75963479e-02  1.91180407e-02 -7.22911485e+00]]
