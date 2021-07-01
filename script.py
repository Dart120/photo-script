
import subprocess
import os
batcmd="system_profiler SPUSBDataType"
connected_devices = subprocess.check_output(batcmd, shell=True)

if "/Volumes/CAMERA" in str(connected_devices):
    setOnCamera = set(os.listdir("/Volumes/CAMERA/DCIM/102MSDCF"))
    setOnComp = set(os.listdir("/Users/temi/Pictures"))
    for i in setOnCamera.difference(setOnComp):
        os.system('cp /Volumes/CAMERA/DCIM/102MSDCF/{} /Users/temi/Pictures/{}'.format(i,i))