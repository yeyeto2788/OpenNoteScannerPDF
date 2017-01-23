#!/usr/bin/env python

__author__ = "Juan Biondi"
__credits__ = ["Juan Biondi"]
__version__ = "0.1"
__maintainer__ = "Juan Biondi"

__status__ = "Development"

"""
Import Modules needed for this script.
"""
import os, qrcode, glob, re

from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.units import inch
from reportlab.platypus import Image as PDFImage




"""
Declare functions for the code.
"""

class GeneratePage(object):
    """
    Class object to call different functions to create the images needed to
    generate the PDF files.
    """
    DirectoryName="/QR_Images/"
    BackgroundName="Background.png"

        
    def __init__(self, FileName, PDF_Name):
            """
            Init function to have the variables in the class
            """
            self.FileName=FileName
            self.PDF_Name=PDF_Name
   
    def CreateBackgroud(self):
        """
        This function will generate a blank page A4 based on 300dpi.
        
        2475 X 3525 ((300 X 8.25) X (300 X 11.75))
        """
        TempName1="Black.png"
        TempName2="white.png"
        im= Image.new("RGB", (2475, 3525), "#ffffff")
        im.save(self.BackgroundName, "PNG")
        im1= Image.new("RGB", (2175, 3225), "#000000")
        im1.save(TempName1, "PNG")
        im2= Image.new("RGB", (2075, 3125), "#ffffff")
        im.save(TempName2, "PNG")
        bottom=Image.open(self.BackgroundName)
        middle=Image.open(TempName1)
        top=Image.open(TempName2)
        bottom.paste(middle, (95,95))
        bottom.paste(top, (125,125))
        bottom.save(self.BackgroundName, "PNG")
        os.remove(TempName1)
        os.remove(TempName2)

                                        
    def create_directory(self):
            """
            This fucntion will check whether directory to create image exist or not.

            If exits will return True so create_images() can proceed to generate the images.

            If it does not exit it will generate the directory and return True to generate
            the images on directory.
            """
            if(os.path.isdir(self.DirectoryName)):
                    print "No need to create directory"
                    return True
            else:
                    os.mkdir(self.DirectoryName)
                    print "Directory created" + os.getcwd()+ self.DirectoryName
                    return True
                
    def create_images(self):
            """
            This function will generate 50 .png images with a string data replacing last character on the
            string in order to have a uniques QR codes and names.
                
            Just have to declare a String variable with the name. It has to be longer that 3 characters.
            """
                
                
            if (self.create_directory()):
                    os.chdir(os.getcwd() + self.DirectoryName)
                    for i in range(1,51):
                            FinalFileName = self.FileName[:-len(str(i))] + str(i)
                            #print "Creating QR data image based on: %s.png" %FinalFileName
                            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
                            qr.add_data(FinalFileName)
                            qr.make(fit=True)
                            img = qr.make_image()
                            with open('%s.png'%FinalFileName, 'wb') as f:
                                    img.save(f)
                            self.CreateBackgroud()

       
    def GenerateCompleteImage(self):
        """
        Paste QR codes into background images       
        """
        self.create_images()
        for i in os.listdir(os.getcwd()):
            if (i.endswith(".png") and (not i.startswith(self.BackgroundName))):
                background=Image.open(self.BackgroundName)
                image=Image.open(i)
                background.paste(image, (2063,3113))
                background.save(i,"PNG")
                #print "Full image %s created." %i

    def CreatePDF(self):
        """
        Create the PDF based on the images in directory.       
        """
        filename = self.PDF_Name
        doc = SimpleDocTemplate(filename,pagesize=A4,
                                rightMargin=0,leftMargin=0,
                                topMargin=0,bottomMargin=0)
        PDF_File=[]
        width = 8.5*inch
        height = 11.5*inch    
        pictures = os.listdir(os.getcwd())
        x = 0

        for pic in pictures:
            if (pic.endswith(".png") and (not pic.startswith("Background.png"))):
                print pic
                im = PDFImage(pic, width, height)
                PDF_File.append(im)
                PDF_File.append(PageBreak())
                x += 1
         
        doc.build(PDF_File)
        print "%s created" % filename


        
Name = "P01 V05 S0000000"
PDF="Final.pdf"
ObjetoALlamar = GeneratePage(Name,PDF)
ObjetoALlamar.GenerateCompleteImage()
ObjetoALlamar.CreatePDF()
print "\nDone"
