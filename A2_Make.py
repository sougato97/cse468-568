# Assignment 2 - CSE 568 Grading Script - Make

import os,sys
import subprocess as sbp


path = sys.argv[1]

files = os.listdir(path)

#sbp.run(["mkdir" , path+"/extracted"])

#sbp.run(["catkin_create_pkg" , "lab2" , "std_msgs", "rospy", "roscpp"])

#sbp.run(["mkdir" , "-p",path+"/catkin_es/src"])

# gb = os.getcwd()
gb = path

for file in files:
    #print (file)
    os.chdir(gb+"/"+file)
    print (os.getcwd())
    os.system("catkin_make")
    os.system("source devel/setup.bash")
    os.system("rosrun lab3 lab3.py")


