#!/bin/python3
from genericpath import isfile
import  os 
import sys 
import shutil



if(len(sys.argv) < 4):
    print("not enougth file")
    exit(1)

file_name = sys.argv[1]
limisize  = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):
    logfile_size = os.stat(file_name).st_size
    logfile_size  = logfile_size / 1024


    if(logfile_size >= limisize):
        if(logsnumber > 0 ):
            for currentfile_number in range(logsnumber, 1, -1):
                    scr  = file_name + "_" + str(currentfile_number-1)
                    dst = file_name  + "_" + str(currentfile_number) 
                    if(os.path.isfile(scr) == True):
                        shutil.copyfile(scr, dst)
                        print("Copied" + scr + "to" + dst)
            shutil.copyfile(file_name, file_name + "_1")       
        myfile = open(file_name, "w")
        myfile.close()        
