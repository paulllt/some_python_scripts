#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:06:23 2017

@author: Paul Louie L. Tito
"""

import os
from PIL import Image

basewidth = 300

dir_list = os.listdir("C:/Users/User/Desktop/images")
res = [os.path.join("C:/Users/User/Desktop/images/", i) for i in dir_list]

counter = 0
for i in res:
    counter += 1
    myImage = Image.open(i)
    newImage = os.path.join("C:/Users/User/Desktop/images", "image"+str(counter)+".JPEG")    
    myImage.save(newImage, "JPEG" ,quality=10)



#myImage = Image.open("C:/Users/User/Desktop/letter_s.jpg")


#wpercent = (basewidth/float(myImage.size[0]))
#hsize = int((float(myImage.size[1])*float(wpercent)))
#myImage = myImage.resize((basewidth,hsize), Image.ANTIALIAS)
#myImage.save("C:/Users/User/Desktop/new_letter_s.jpg",optimize=True,quality=85)


#newImage = "C:/Users/User/Desktop/new_letter_s.jpg"
#myImage.save(newImage, "JPEG", quality=20)


