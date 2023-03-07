"""
Simple controller for the API so main logic is out of the endpoint itself.
"""
import os
import threading
import time

from open_note_scanner import pdf_generator
from open_note_scanner import utils


def generate_pdf(str_size: str, qr_data: str, int_pages: int) -> (str, str):
    """
    Actually generate a `.pdf` file by instantiating the `pdf_generator.PDFGenerator`
    object and call its `generate_pdf` method with the given arguments.

    Args:
        str_size: Size of the page.
        qr_data: Data to be added in the QR code.
        int_pages: Number of pages to be created.

    Returns:
        Tuple with the name of the file and its directory.
    """
    thread_id = threading.get_ident()

    utils.delete_pdfs(thread_id, True)
    pdf = pdf_generator.PDFGenerator(
        qr_data, "{}.pdf".format(str(int(time.time()))), int_pages
    )
    pdf_route = pdf.generate_pdf(str_size, bln_delete=True)

    pdf_file = os.path.basename(pdf_route)
    pdf_directory = os.path.dirname(pdf_route)

    return pdf_file, pdf_directory
