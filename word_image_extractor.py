#!/usr/bin/env python

#Author: Paul Louie L. Tito
#Date: March 16, 2017
#Purpose: Extract images from a Word document

import zipfile, os, shutil


class Extractor:

    def __init__(self, word_doc, target_dir):
        self.word_doc = word_doc
        self.target_dir = target_dir
        
    def Extraction(self):
        images = zipfile.ZipFile(self.word_doc)
        images.extractall(self.target_dir)

    def MoveFiles(self, dirTarget, dirDestination):
        self.dirTarget = dirTarget
        self.dirDestination = dirDestination

        dirImage = os.listdir(self.dirTarget)
        images = [os.path.join(self.dirTarget+"/", i) for i in dirImage]

        for image in images:
            shutil.move(image,self.dirDestination)
            
    def RemoveDirectories(self, folders):
        self.folders = folders

        f = os.listdir(self.folders)
        paths = [os.path.join(self.folders+"/", j) for j in f]

        for path in paths:
            if os.path.isdir(path) == True:
                shutil.rmtree(path)

    def RemoveContentTypes(self, rmFile):
        self.rmFile = rmFile
        os.remove(rmFile)


if __name__ == '__main__':
    e = Extractor("csit_week2016.docx", "C:/Users/User/Desktop/images/")
    e.Extraction()
    e.MoveFiles("C:/Users/User/Desktop/images/word/media", "C:/Users/User/Desktop/images")
    e.RemoveDirectories("C:/Users/User/Desktop/images")
    e.RemoveContentTypes("C:/Users/User/Desktop/images/[Content_Types].xml")
        
        
    
