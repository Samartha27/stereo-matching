import json
import numpy as np

def left(filename):
    camera_left = json.load(open(filename))

    intrinsic_left = np.zeros((3,4))
    extrinsic_left = np.zeros((4,4))



    k = 0
    break_out_flag = False
    for i in range(len(intrinsic_left[0])):
        for j in range(len(intrinsic_left[1])):
            if k < len(camera_left["intrinsic"]):
                intrinsic_left[i][j] = camera_left["intrinsic"][k]
                k +=1
            else:
                break_out_flag = True
                break
        if break_out_flag:
            break

    k = 0
    break_out_flag = False
    for i in range(len(extrinsic_left[0])):
        for j in range(len(extrinsic_left[1])):
            if k < len(camera_left["extrinsic"]):
                extrinsic_left[i][j] = camera_left["extrinsic"][k]
                k +=1
            else:
                break_out_flag = True
                break
        if break_out_flag:
            break
    #print(intrinsic_left)
    #print(extrinsic_left)

    return intrinsic_left,extrinsic_left


def right(filename):
    camera_right = json.load(open(filename))

    intrinsic_right = np.zeros((3,4))
    extrinsic_right = np.zeros((4,4))
    k = 0
    break_out_flag = False
    for i in range(len(intrinsic_right[0])):
        for j in range(len(intrinsic_right[1])):
            if k < len(camera_right["intrinsic"]):
                intrinsic_right[i][j] = camera_right["intrinsic"][k]
                k +=1
            else:
                break_out_flag = True
                break
        if break_out_flag:
            break

    k = 0
    break_out_flag = False
    for i in range(len(extrinsic_right[0])):
        for j in range(len(extrinsic_right[1])):
            if k < len(camera_right["extrinsic"]):
                extrinsic_right[i][j] = camera_right["extrinsic"][k]
                k +=1
            else:
                break_out_flag = True
                break
        if break_out_flag:
            break
    
    #print(intrinsic_right)
    #print(extrinsic_right)

    return intrinsic_right,extrinsic_right



