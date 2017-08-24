#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Juan Biondi"
__credits__ = ["Juan Biondi"]
__version__ = "0.2"
__maintainer__ = "Juan Biondi"

__status__ = "Development"

"""
Import Modules
"""


import qrcode
import os

"""
Declare functions
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
EXECUTE THE CODE.
"""


Name = "P01 V05 S0000000"
QR=GenerateQR(Name)
QR.create_images()
