#!/usr/bin/env python

__author__ = "Juan Biondi"
__credits__ = ["Juan Biondi"]
__version__ = "0.1"
__maintainer__ = "Juan Biondi"

__status__ = "Development"

"""
Import Modules needed for this script.
"""
import qrcode
import os

"""
Declare functions for the code.
"""
class GenerateQR(object):
        """
        Global class to have it more like OOP
        """
        
        def __init__(self, FileName):
                """
                Init function to have the variables in the class
                """
                self.FileName=FileName

        def create_images(self):
                """
                This function will generate 50 .png images with a string data replacing last character on the
                string in order to have a uniques QR codes and names.
                
                Just have to declare a String variable with the name. It has to be longer that 3 characters.
                """
                

                for i in range(1,51):
                        FinalFileName = self.FileName[:-len(str(i))] + str(i)
                        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
                        qr.add_data(FinalFileName)
                        qr.make(fit=True)
                        img = qr.make_image()
                        with open('%s.png'%FinalFileName, 'wb') as f:
                                img.save(f)

        
                        
"""
Call the function(s) to be used on the final code.
"""



Name = "P01 V05 S0000000"
QR=GenerateQR(Name)
QR.create_images()

