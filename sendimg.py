#!/usr/bin/env python3

from PIL import Image
import sys
import struct
import os

a=Image.open(sys.argv[1])
pal_image= Image.new("P", (1,1))
pal_pal = [0,0,0,255,0,0,0,255,0,0,0,255,255,255,255]
pal_pal.extend((0,0,0)*(256-5))
pal_image.putpalette(pal_pal)
a=a.convert("RGB")
a=a.quantize(method=Image.LIBIMAGEQUANT,palette=pal_image)
a=a.convert("RGB")
width, height = a.size

proc=Image.new(a.mode, ((width+7)//8*8, height), (255,255,255))
proc.paste(a)
proc.save("img.png")
width, height = proc.size

hpack = 1024//(width//8*4)

cdict = {
        0: lambda c: c == (0,0,0),
        1: lambda c: c == (0,0,255),
        2: lambda c: c == (0,255,0),
        3: lambda c: c == (255,0,0),
        }
for y in range(0,height,hpack):
    hc = min(hpack,height-y)
    tosend = struct.pack("BB",hc,(width+7)//8)
    for yp in range(hc):
        for c in range(4):
            for x in range(0,width,8):
                byte = 0
                byte |= 0x00 if cdict[c](proc.getpixel((x+0,y+yp))) else 0x80
                byte |= 0x00 if cdict[c](proc.getpixel((x+1,y+yp))) else 0x40
                byte |= 0x00 if cdict[c](proc.getpixel((x+2,y+yp))) else 0x20
                byte |= 0x00 if cdict[c](proc.getpixel((x+3,y+yp))) else 0x10
                byte |= 0x00 if cdict[c](proc.getpixel((x+4,y+yp))) else 0x08
                byte |= 0x00 if cdict[c](proc.getpixel((x+5,y+yp))) else 0x04
                byte |= 0x00 if cdict[c](proc.getpixel((x+6,y+yp))) else 0x02
                byte |= 0x00 if cdict[c](proc.getpixel((x+7,y+yp))) else 0x01
                tosend+=bytes([byte])
    open("part.bin","wb").write(tosend)
    os.system("./build/pocktool/bin2wav -p 1500 -t bin -a 0 part.bin part.wav")
    os.system("./cload.sh part.wav")
open("part.bin","wb").write(b"\x00\x00")
os.system("./build/pocktool/bin2wav -p 1500 -t bin -a 0 part.bin part.wav")
os.system("./cload.sh part.wav")
