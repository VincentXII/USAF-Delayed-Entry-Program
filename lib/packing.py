### This is the main screen where you select where you want to go. Had to split it up in many parts because it would of been awful to include all of this in one python file ###

import subprocess, sys, os, shutil, platform 
from VXGUI.StdColors import red
from VXGUI.Geometry import offset_rect, rect_sized
from VXGUI import Window, Image, View, Button, Label, application
from VXGUI.Alerts import note_alert
win = Window(title = "Packing")

def packing():
	import packing

## Image ##
class ImageTestView(View):

    def draw(self, c, r):
        #c.backcolor = yellow
        c.erase_rect(r)
        main_image_pos = (0, 0)
        src_rect = (image.bounds)
        dst_rect = offset_rect(src_rect, main_image_pos)
        image.draw(c, src_rect, dst_rect)


## Buttons ##
bt = [
    Button("YOU SHOULD SEE THIS IF IT WORKED", action = packing),
]

## Label and Image Placement ##
image_path = "images/packing.png"
image = Image(file = image_path)
view = ImageTestView(size = (815,480))
win.add(view)

## Building the window ##
win.place_column(bt, left = 200, top = 330)
win.size = (815, 960)
win.show()
application().run() 
