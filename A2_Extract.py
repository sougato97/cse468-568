# Assignment 2 - CSE 568 Grading Script - Extract

import os,sys
import subprocess as sbp


path = sys.argv[1]

files = os.listdir(path)

sbp.run(["mkdir" , path+"/extracted"])

for file in files:
    if file[-4:] == '.zip':
        print (file[13:-4])
        sbp.run(["mkdir" ,"-p", path+"/extracted"+"/"+file[13:-4]+"/src"])
        sbp.run(["unzip" , path+"/"+file[:-4], "-d", path+"/extracted"+"/"+file[13:-4]+"/src"])
        print (file)


