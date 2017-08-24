#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Juan Biondi"
__credits__ = ["Juan Biondi"]
__version__ = "0.2"
__maintainer__ = "Juan Biondi"

__status__ = "Development"

"""
Import modules
"""
import qrcode


"""
EXECUTE THE CODE.
"""

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )

qr.add_data("https://google.com")
qr.make(fit=True)
img = qr.make_image()

FileName = "P01 V05 S0000000"

with open(FileName, 'wb') as f:
		img.save(f)
