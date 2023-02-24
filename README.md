# stereo-matching

## Implementation

For Epipolar directory, run 2 commands as mentioned below:\
Generate points \
`python data/generate_points.py`

Generate plot \
`python tools/epipolar_geometry.py --r_img ./data/right.jpg --l_img ./data/left.jpg`



For Epiploar_json directory, only run: \
 `python tools/generate_fundamental.py  --l_img ./data/c078.jpg  
                                        --r_img ./data/c076.jpg  
                                        --l_keypoints  /Users/stlp/Desktop/sam/ram/pose/vis_results/c078/keypoints.json  
                                        --r_keypoints  /Users/stlp/Desktop/sam/ram/pose/vis_results/c076/keypoints.json --frames 9250` \
 or \
 `python tools/generate_fundamental.py  --l_img ./data/c078.jpg  
                                        --r_img ./data/c076.jpg  
                                        --l_keypoints  /Users/stlp/Desktop/sam/ram/pose/vis_results/c078/keypoints.json  
                                        --r_keypoints  /Users/stlp/Desktop/sam/ram/pose/vis_results/c076/keypoints.json --frames 9250 9251`
## Sample output:
Fundamental matrix : \
 [[ 9.93947782e-07 -4.48011207e-05  1.63459154e-02] \
 [ 3.93890229e-05 -4.98987293e-06  2.40110466e-03] \
 [-1.75963479e-02  1.91180407e-02 -7.22911485e+00]]
