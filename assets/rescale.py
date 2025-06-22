from PIL import Image, ExifTags
import os
import math
import numpy as np

start_path = "./item"

def fixFile(x, apath):
    with Image.open(apath + "/" + x) as item:
        exif_data = item._getexif()
        isResized = False
        if exif_data:
            isResized = exif_data.get(1,False)
#            print(exif_data.get(283, 0))
#            for tag, value in exif_data.items():
#                tag_name = ExifTags.TAGS.get(tag, tag)
#                print(f"{tag_name} = {tag}: {value}")
        if isResized:
            print("[FAIL]" + x + " is already resized")
            return
        else:
            exif_data = Image.Exif()
            exif_data[1] = True
            output = item
            maxcolors = -1
            try:
                maxcolors = len(item.getcolors(maxcolors = 64))
                print("[SUCCESS] " + str(maxcolors) + " : " + x)
                if item.mode != 'P':
                    output = item.convert(mode = 'P', palette = 1, colors = maxcolors)
                output = output.resize(size= (item.width * 2, item.height * 2), resample = 0 )
            except:
                print("[SUCCESS] too many" + " : " + x)
                output = output.resize(size= (item.width * 2, item.height * 2), resample = 0 )
            output.save(apath + "/" + x, exif = exif_data)

def fix_sprite(item, angle, output):
    for x in range(0,16):
        for y in range(0,16):
            thiscolor = item.getpixel( (x, y) )
            output.putpixel( (x, y), (thiscolor[0], thiscolor[1], thiscolor[2], int(255 * (3/5)) ) )


def fixFolder(apath):
    for x in os.listdir(path = apath):
        if x.endswith(".png"):
            fixFile(x, apath)
        else:
            try:
                print(f"{x} is a ... folder? Probably? ahhh, screw it.")
                fixFolder(apath + "/" + x)
            except:
                print("shoot, that was not a folder. >_>")

fixFolder(start_path)

