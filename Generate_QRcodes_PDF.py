#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = "Juan Biondi"
__credits__ = ["Juan Biondi"]
__version__ = "0.2"
__maintainer__ = "Juan Biondi"

__status__ = "Development"

"""
Import Modules needed
"""

import os
import qrcode
import glob
import re

from PIL import Image
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.units import inch
from reportlab.platypus import Image as PDFImage
from reportlab.pdfgen import canvas


"""
Declare functions
"""


class GeneratePage(object):
    """
    Class object to call different functions to create the images needed to
    generate the PDF files.
    """
    DirectoryName = "QR_Images" + os.sep
    BackgroundName = "Background.png"


    def __init__(self, FileName, PDF_Name, MaxPages):
            """
            Init function to have the variables in the class
            """
            self.FileName = FileName
            self.PDF_Name = PDF_Name
            self.MaxPages = MaxPages


    def create_directory(self):
            """
            This fucntion will check whether directory to create image exist or not.
            If exits will return True so create_images() can proceed to generate the images.
            If it does not exit it will generate the directory and return True to generate
            the images on directory.
            """
            DirectoryCheck = os.path.join(os.getcwd(), self.DirectoryName)
            if(os.path.exists(os.path.join(os.getcwd(), self.DirectoryName))):
                    print ("No need to create directory")
                    return True
            else:
                    os.mkdir(self.DirectoryName)
                    print ("Directory created" + os.path.join(os.getcwd(), self.DirectoryName))
                    return True


    def create_images(self):
            """
            This function will generate 50 .png images with a string data replacing last character on the
            string in order to have a uniques QR codes and names.
            Just have to declare a String variable with the name. It has to be longer that 3 characters.
            """


            if (self.create_directory()):
                    os.chdir(os.path.join(os.getcwd(), self.DirectoryName))
                    for i in range(1,self.MaxPages+1):
                            FinalFileName = self.FileName[:-len(str(i))] + str(i)
                            #print "Creating QR data image based on: %s.png" %FinalFileName
                            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
                            qr.add_data(FinalFileName)
                            qr.make(fit=True)
                            img = qr.make_image()
                            with open('%s.png'%FinalFileName, 'wb') as f:
                                    img.save(f)


    def GeneratePDF(self):
        """
        Create the PDF based on the images in directory.
        """
        self.create_images()
        c = canvas.Canvas(self.PDF_Name, pagesize=A4)
        for image in os.listdir(os.getcwd()):
            if image.endswith(".png"):
                # move the origin up and to the left
                c.translate(0, 0)
                # choose some colors
                c.setStrokeColorRGB(0, 0, 0)
                c.setFillColorRGB(0, 0, 0)
                # draw a rectangle
                c.rect(0.1*inch, 0.1*inch, 8.1*inch, 11.4*inch, stroke=0, fill=1)
                c.setFillColorRGB(255, 255, 255)
                c.rect(0.25*inch, 0.25*inch, 7.8*inch, 11.1*inch, stroke=0, fill=1)
                c.drawImage(image, 7*inch, 0.35*inch, width=1*inch, height=1*inch, mask=None)
                c.showPage()
        c.save()
        self.DeleteImages(1)

    def DeleteImages(self, BlnDelete):
        """
        Delete images after PDF is created if BlnDelete==1
        """
        if BlnDelete:
            for image in os.listdir():
                if image.endswith(".png"):
                    os.remove(image)
"""
EXECUTE THE CODE
"""


Name = "P01 V05 S0000000"
PDF = "Final.pdf"
MaximumPages = 50
ObjetoALlamar = GeneratePage(Name, PDF, MaximumPages)
ObjetoALlamar.GeneratePDF()
print ("\nDone")
