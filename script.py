#!/usr/bin/env python
import subprocess
import os
import sys
print('here')
print(sys.argv)
if len(sys.argv) == 3:
    driveName = sys.argv[2]
    cardName = sys.argv[1]
    batcmd="system_profiler SPUSBDataType"
    connected_devices = subprocess.check_output(batcmd, shell=True)
    isCameraConn = "/Volumes/{}".format(cardName) in str(connected_devices)
    isDriveConn = "/Volumes/{}".format(driveName) in str(connected_devices)
    print(isCameraConn,isDriveConn)
    if isCameraConn and isDriveConn:
        setOnCamera = set(os.listdir("/Volumes/{}/DCIM/102MSDCF".format(cardName)))
        setOnComp = set(os.listdir("/Volumes/{}/Pictures"))
        for i in setOnCamera.difference(setOnComp):
            os.system('cp /Volumes/{}/DCIM/102MSDCF/{} /Volumes/{}/Pictures/{}'.format(cardName,i,driveName,i))
    elif not isCameraConn and isDriveConn:
        print("Error:The camera isnt connected")

    elif isCameraConn and not isDriveConn:
        print("Error: The drive isnt connected")
    else:
        print('Neither device is connected')
else:
    print('Error: [Name of sd card] [Name of drive]')