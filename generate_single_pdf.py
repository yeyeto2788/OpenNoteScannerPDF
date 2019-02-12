#!/usr/bin/env python
# -*- coding: utf-8 -*-
from open_note_scanner import utils
from open_note_scanner.pdf_generator import PDFGenerator


print(utils.BASE_PATH)
print(utils.QR_DIR)
print(utils.PDF_DIR)

qr_data = "P01 V05 S"
PDF = "Final.pdf"
MaximumPages = 2

pdf = PDFGenerator(qr_data, PDF, MaximumPages)
pdf.generate_pdf('A4', bln_delete=1)
