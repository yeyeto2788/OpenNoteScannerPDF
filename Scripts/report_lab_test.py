#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


def generate_background():
    """
    Generate the PDF to test creation of it
    """
    c = canvas.Canvas("hello.pdf", pagesize=A4)
    for image in os.listdir(os.getcwd()):
        if image.endswith(".png"):
            # move the origin up and to the left
            c.translate(0, 0)
            # choose some colors
            c.setStrokeColorRGB(0, 0, 0)
            c.setFillColorRGB(0, 0, 0)
            # draw a rectangle
            c.rect(0.1 * inch, 0.1 * inch, 8.1 * inch, 11.4 * inch, stroke=0, fill=1)
            c.setFillColorRGB(255, 255, 255)
            c.rect(0.25 * inch, 0.25 * inch, 7.8 * inch, 11.1 * inch, stroke=0, fill=1)
            c.drawImage(
                image, 7 * inch, 0.35 * inch, width=1 * inch, height=1 * inch, mask=None
            )
            c.showPage()
    c.save()


generate_background()
