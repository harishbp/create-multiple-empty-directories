import os

FOLDER_NAME = "tsk"
FOLDER_START_POINT = 22
FOLDER_END_POINT = 30

for i in range(FOLDER_START_POINT,FOLDER_END_POINT+1):
    try:  
        os.mkdir(FOLDER_NAME+str(i))
    except OSError:  
        print ("Failed to create directory",FOLDER_NAME+str(i))
    else:  
        print ("directory created Successfully",FOLDER_NAME+str(i))
