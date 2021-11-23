import PIL
from PIL import Image
import numpy as np
import random
#***********IMPORTANT FUNCTIONS START***********

def rgbValue(arr):
    return [arr[0],arr[1],arr[2]]

def AllComb(x,y):

    arr=[]

    for i in range(x):
        for i2 in range(y):
            arr.append((i,i2))

    return arr


def imageCopy(image):
    x, y = image.size
    im = PIL.Image.new(mode="RGB", size=(x, y))

    arr = AllComb(x,y)
    for i in arr:
        [r,g,b] = rgbValue(image.getpixel(i))
        im.putpixel(i,(r,g,b))

    return im

#***********IMPORTANT FUNCTIONS END***********


# in this method , input parameter are the file names
def similarityFN(filename,filename2,fluctuation):
    f = fluctuation
    im = PIL.Image.open(filename)
    im2 = PIL.Image.open(filename2)

    x,y = im.size
    x2,y2 = im2.size
    

    im2c = imageCopy(im2)
    im2c = im2c.resize((x,y))


    index = 0

    arr = AllComb(x,y)
    for i in arr:
        [r,g,b] = rgbValue(im.getpixel(i))
        [r2,g2,b2] = rgbValue(im2c.getpixel(i))

        if (r + f) >= r2 and r2 >= (r - f) and (g + f) >= g2 and g2 >= (g - f) and (b + f) >= b2 and b2 >= (b - f):
            index += 1

    return index/len(arr)

#in this method , input parameters are the image objects
def similarity(im,im2):
    x,y = im.size
    x2,y2 = im2.size


    im2c = imageCopy(im2)
    im2c = im2c.resize((x,y))

    index = 0

    arr = AllComb(x,y)
    for i in arr:
        [r,g,b] = rgbValue(im.getpixel(i))
        [r2,g2,b2] = rgbValue(im2c.getpixel(i))

        if r == r2 and g == g2 and b == b2:
            index += 1

    return index/x*y


def toBW(image):

    x,y = image.size
    arr = AllComb(x,y)
    im = PIL.Image.new(mode="RGB",size = (x,y))

    for i in arr:
        [r,g,b] = rgbValue(image.getpixel(i))
        mx = max(max(r,g),b)
        im.putpixel(i,(mx,mx,mx))

    return im

def noise(image,noiseAm):

    x, y = image.size
    arr = AllComb(x, y)
    im = PIL.Image.new(mode="RGB", size=(x, y))

    for i in arr:
        [r,g,b] = rgbValue(image.getpixel(i))
        r += random.randint(-noiseAm,noiseAm)
        g += random.randint(-noiseAm,noiseAm)
        b += random.randint(-noiseAm,noiseAm)
        im.putpixel(i,(r,g,b))

    return im
