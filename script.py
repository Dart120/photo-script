#!/usr/bin/env python
import subprocess
import os
import sys
if len(sys.argv) == 3:
    driveName = sys.argv[2]
    cardName = sys.argv[1]
    batcmd="system_profiler SPUSBDataType"
    connected_devices = subprocess.check_output(batcmd, shell=True)
    isCameraConn = "/Volumes/{}".format(cardName) in str(connected_devices)
    isDriveConn = "/Volumes/{}".format(driveName) in str(connected_devices)
    if isCameraConn and isDriveConn:
        if not os.path.exists("/Volumes/{}/Pictures".format(driveName)):
            os.makedirs("/Volumes/{}/Pictures".format(driveName))
        setOnCamera = set(os.listdir("/Volumes/{}/DCIM/102MSDCF".format(cardName)))
        setOnComp = set(os.listdir("/Volumes/{}/Pictures".format(driveName)))
        for i in setOnCamera.difference(setOnComp):
            os.system('cp /Volumes/{}/DCIM/102MSDCF/{} /Volumes/{}/Pictures/{}'.format(cardName,i,driveName,i))
            print(i)
    elif not isCameraConn and isDriveConn:
        print("Error: The camera isn't connected")

    elif isCameraConn and not isDriveConn:
        print("Error: The drive isn't connected")
    else:
        print('Error: Neither device is connected')
else:
    print('Error: [Name of sd card] [Name of drive]')