"""

Main logic of pdf creating using reportlab modules.

The pdf files are created based on argument passed to the
class `PDFGenerator`

"""
import os
import qrcode

from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from open_note_scanner import utils

SIZES = {
    'A4': A4,
    'Letter': letter
}


class PDFGenerator:
    """
    Class object to call different functions to create the images needed to
    generate the PDF files.

    """
    base_dir = utils.BASE_PATH
    qr_directory = utils.QR_DIR
    pdf_directory = utils.PDF_DIR
    bg_image_name = "BG.png"

    def __init__(self, str_qr_data, pdf_name, int_pages):
        """
        Constructor method to have the variables in the class

        Args:
            str_qr_data: Data that the qr code will contain.
            pdf_name: Name of the pdf file.
            int_pages: Number of pages that pdf will have.

        """
        self.qr_data = str_qr_data + '-0000000'
        self.pdf_name = pdf_name
        self.max_pages = int_pages

    def create_images(self):
        """
        This function will generate .png images with a string data replacing
        last characters of the string by the number of iteration in order to
        have a uniques QR codes and names.

        """

        if utils.create_directory():
            # Go to QR images directory.
            os.chdir(self.qr_directory)
            for int_index in range(1, (self.max_pages + 1)):
                final_file_name = self.qr_data[:-len(str(int_index))] + str(int_index)
                qr_img = qrcode.QRCode(version=1,
                                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                                       box_size=10,
                                       border=4, )
                qr_img.add_data(final_file_name)
                qr_img.make(fit=True)
                img = qr_img.make_image()
                with open('%s.png'%final_file_name, 'wb') as qr_img_file:
                    img.save(qr_img_file)
            # Return to the base directory.
            os.chdir(self.base_dir)

    def generate_pdf(self, size='A4', bln_delete=1):
        """
        Create the PDF based on the images in QR directory.

        Args:
            size: size of the paper.
            bln_delete: boolean to delete or not previous runs.

        Returns:
            String with the directory where the `.pdf` was created.
        """
        self.create_images()
        # Go to PDFs directory
        os.chdir(self.pdf_directory)

        page_width = SIZES[size][0]
        page_height = SIZES[size][1]

        # Define sizes for all boxes and X,Y location of QR images.
        if size == 'A4':

            bk_width = page_width - 10.4
            bk_height = page_height - 70.4
            wt_width = page_width - 32
            wt_height = page_height - 91.6
            bk_x = 10
            bk_y = 10
            wt_x = 20
            wt_y = 20

        else:
            bk_width = page_width - 14.4
            bk_height = page_height - 14.4
            wt_width = page_width - 36
            wt_height = page_height - 36
            bk_x = inch / 10
            bk_y = inch / 10
            wt_x = inch / 4
            wt_y = inch / 4

        qr_width = inch
        qr_height = inch
        qr_x = page_width - 95
        qr_y = 30

        pdf_canvas = canvas.Canvas(self.pdf_name, pagesize=size)

        lst_files = os.listdir(self.qr_directory)
        print(lst_files)
        print(utils.sort_alphanumeric_list(lst_files))

        for image_file in utils.sort_alphanumeric_list(lst_files):

            if image_file.endswith(".png"):
                # Move the origin up and to the left
                pdf_canvas.translate(0, 0)
                # Draw a black rectangle
                pdf_canvas.setStrokeColorRGB(0, 0, 0)
                pdf_canvas.setFillColorRGB(0, 0, 0)
                pdf_canvas.rect(bk_x, bk_y, bk_width, bk_height, stroke=0, fill=1)
                # Draw a white rectangle
                pdf_canvas.setFillColorRGB(255, 255, 255)
                pdf_canvas.rect(wt_x, wt_y, wt_width, wt_height, stroke=0, fill=1)

                image_dir = os.path.join(self.qr_directory, image_file)
                # Add QR image into canvas
                pdf_canvas.drawImage(image_dir, qr_x, qr_y,
                                     width=qr_width, height=qr_height, mask=None)
                pdf_canvas.showPage()
        pdf_canvas.save()

        if bln_delete:
            utils.delete_images(bln_delete)
        # Return to based directory
        os.chdir(self.base_dir)

        return os.path.join(self.pdf_directory, self.pdf_name)
