import cv2


"""folder = {'S001/':['c001/','c002/','c003/','c004/','c005/','c006/','c007/'],
          'S003/':['c014/','c015/','c016/','c017/','c018/','c019/'],
          'S009/':['c047/','c048/','c049/','c050/','c051/','c052/'],
          'S014/':['c076/','c077/','c078/','c079/','c080/','c081/'],
          'S022/':['c124/','c125/','c126/','c127/','c128/','c129/']}

for k,v in folder.items():
    for i in range(len(v)):
        root = k + v[i]
        print(root)"""
root = 'S014/c078/'

video_path = root + 'video.mp4'
output_path = root +'left.jpg'

vidcap = cv2.VideoCapture(video_path)
vidcap.set(cv2.CAP_PROP_POS_MSEC,308350)    
success,image = vidcap.read()
if success:
    cv2.imwrite(output_path, image)
    cv2.imshow("output",image)
    cv2.waitKey()