#!/usr/bin/env python
# -*- coding: utf-8 -*-
from open_note_scanner.pdf_generator import PDFGenerator

QR_DATA = "P01 V05 S"
PDF_NAME = "Final.pdf"
MAX_PAGES = 2

PDF = PDFGenerator(QR_DATA, PDF_NAME, MAX_PAGES)
PDF.generate_pdf('A4', bln_delete=1)
