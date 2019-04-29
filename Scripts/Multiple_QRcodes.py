#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Juan Biondi"
__credits__ = ["Juan Biondi"]
__version__ = "0.3"
__maintainer__ = "Juan Biondi"

__status__ = "Development"

import qrcode


def create_images(filename):
        """
        This function will generate 50 .png images with a string data replacing last
        character on the string in order to have a uniques QR codes and names.

        Just have to declare a String variable with the name. It has to be longer
        that 3 characters.

        Args:
            filename: data and name for the images.

        Returns:
            None
        """

        for i in range(1, 51):
                final_name = filename[:-len(str(i))] + str(i)
                qr = qrcode.QRCode(
                        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10, border=4, )
                qr.add_data(final_name)
                qr.make(fit=True)
                img = qr.make_image()
                with open('%s.png' % final_name, 'wb') as f:
                        img.save(f)


Name = "P01 V05 S0000000"
create_images(Name)
