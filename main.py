### This is the main screen where you select where you want to go. Had to split it up in many parts because it would of been awful to include all of this in one python file ###

import subprocess, sys, os, shutil, platform, os.path, pathlib, linecache
from pathlib import Path
from VXGUI.StdButtons import DefaultButton, CancelButton
from VXGUI.StdFonts import system_font
from VXGUI.StdColors import blue
from VXGUI.Geometry import offset_rect, rect_sized
from VXGUI import Window, ModalDialog, Image, View, Font, Button, Label, \
    TextField, application

from VXGUI.Alerts import note_alert
win = Window(title = "USAF Delayed Entry Program")


## File Integrity Check ##
userinfo = Path("userinfo.ini")
if userinfo.is_file():
	print("File Integrity Pass")
else:
	print("Creating userinfo.ini")
	ff2 = open("userinfo.ini","w")
	ff2.close()


## Button Commands ##
def packing():
	os.startfile("lib\packing.py")

def write(lastname, startdate):
	usrwrite = open("userinfo.ini","w") 
	usrwrite.write(lastname.text)
	usrwrite.write("\n")
	usrwrite.write(startdate.text)
	usrwrite.close()


def editbmttime():
    win = Window(size = (480, 200), title = "Welcome to Delayed Entry Program")
    lastnamelbl = Label(text = "Please Enter Last Name", position = (20, 20))
    lastname = TextField(position = (20, 40), width = 200)
    startdatelbl = Label(text = "Please Enter Start Date (mm/dd/yyyy)", position = (20, 70))
    startdate = TextField(position = (20, 90), width = 200)
    ok = Button("OK", position = (20, 130),	action = (write, lastname, startdate))
    win.add(lastnamelbl)
    win.add(lastname)
    win.add(startdatelbl)
    win.add(startdate)
    win.add(ok)
    win.show()

def exit():
	os._exit(0)

## Image ##
class ImageTestView(View):

    def draw(self, c, r):
        #c.backcolor = yellow
        c.erase_rect(r)
        main_image_pos = (0, 0)
        src_rect = (image.bounds)
        dst_rect = offset_rect(src_rect, main_image_pos)
        image.draw(c, src_rect, dst_rect)

## Getting BMT Text ##
lastnamread = open("userinfo.ini", "r")
last_name = lastnamread.readline()
lastnamread.close()

start_date = linecache.getline("userinfo.ini", 2)


## Label and Image Placement ##
big = Font("Consolas", 2 * system_font.size, ['bold'])
image_path = "images/main.png"
image = Image(file = image_path)
view = ImageTestView(size = (815,480))
showlastname = Label(text = "Welcome " + last_name, position = (300, 490), font = big, color = blue)
showbmtdate = Label(text = "BMT Start Date: " + start_date, position = (260, 520), font = big, color = blue)
win.add(view)
win.add(showlastname)
win.add(showbmtdate)


## Buttons ##
bt = [
    Button("Packing", action = packing),
]
updatebmt = Button("Update BMT Date", position = (320, 550) ,action = editbmttime)
win.add(updatebmt)

## Building the window ##
win.place_column(bt, left = 170, top = 520)
win.size = (815, 900)
win.show()
application().run() 
