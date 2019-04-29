"""
Simple API for generating the `.pdf` file within the server and return it already generated.

"""
import os
import time

import flask
import flask_restful

from open_note_scanner import utils
from open_note_scanner import pdf_generator


class APIGenerator(flask_restful.Resource):
    """
    `.pdf` file server API to send the pdf files to the clients doing a get request.

    """

    @staticmethod
    def get(str_size, qr_data, int_pages):
        """
        Return the File from server if exists on the filesystem.

        This will do a check whether the size is either `A4` or `letter`, then it checks
        for the length of the `qr_data` argument and finally if will generate the `.pdf`
        file returning it to the client.

        """

        if str_size == 'A4' or 'letter':
            qr_len = len(qr_data)

            if qr_len > 4:

                utils.delete_pdfs(1)
                pdf = pdf_generator.PDFGenerator(qr_data,
                                                 '{}.pdf'.format(str(int(time.time()))),
                                                 int_pages)
                pdf_route = pdf.generate_pdf(str_size, bln_delete=1)

                pdf_file = os.path.basename(pdf_route)
                pdf_directory = os.path.dirname(pdf_route)

                api_return = flask.send_from_directory(pdf_directory, pdf_file, as_attachment=True)
            else:
                api_return = flask_restful.abort(
                    404, error_message="QR data length should be higher than 4.")

        else:
            api_return = flask_restful.abort(404, error_message="Please check size.")

        return api_return
