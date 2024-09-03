import PIL
from PIL import Image
import os

mywidth = 2000
source_dir = "C:/Users/91843/Desktop/project-assets/source"
destination_dir = "C:/Users/91843/Desktop/project-assets/dest"

def resize_image(old_pic, new_pic, mywidth):
    
    img = Image.open(old_pic)
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth,hsize), PIL.Image.LANCZOS)
    img.save(new_pic)

def resize_directory(source_dir, destination_dir, mywidth):
    files = os.listdir(source_dir)
    
    i = 0
    for file in files:
        i+=1
        old_pic = source_dir + "/" + file
        new_pic = destination_dir + "/" + file
        resize_image(old_pic, new_pic, mywidth)
        print("done", i)
        
resize_directory(source_dir, destination_dir,mywidth)

