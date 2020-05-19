import cv2
import os
import glob
folder = 'folder-path-here'
extension = 'extension-here'
video_files = glob.glob(folder+'*.'+extension)
for file_name in video_files:
    vidcap = cv2.VideoCapture(file_name)
    success,image = vidcap.read()
    count = 0
    save_folder = file_name.split('.')[0]
    shortname1 = file_name.split('/')
    shortname2 = shortname1[-1].split('\\')
    shortname3 = shortname2[-1].split('.')
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    while True: # .read() below sometimes returns false in middle of video.
        write_file = save_folder+'/'+shortname3[0]+"frame%d.png" % count
        cv2.imwrite(write_file, image)     # save frame as png file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
