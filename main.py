### This is the main screen where you select where you want to go. Had to split it up in many parts because it would of been awful to include all of this in one python file ###

import subprocess, sys, os, shutil, platform 
from VXGUI.StdColors import red
from VXGUI.Geometry import offset_rect, rect_sized
from VXGUI import Window, Image, View, Button, Label, application
from VXGUI.Alerts import note_alert

def packing():
	os.startfile("lib\packing.py")


## Buttons ##
bt = [
    Button("Packing", action = packing),
]

## Building the window ##
win = Window(title = "USAF Delayed Entry Program")
win.place_column(bt, left = 200, top = 330)
win.size = (815, 960)
win.show()
application().run() 
