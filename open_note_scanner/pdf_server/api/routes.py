"""
Simple API for generating the `.pdf` file within the server and return it already generated.

"""

import flask
import flask_restful

from open_note_scanner.pdf_server.api import controller as controller


class APIGenerator(flask_restful.Resource):
    """
    `.pdf` file server API to send the pdf files to the clients doing a get request.

    """

    @staticmethod
    def get(str_size: str, qr_data: str, int_pages: int):
        """
        Return the File from server if exists on the filesystem.

        This will do a check whether the size is either `A4` or `letter`, then it checks
        for the length of the `qr_data` argument and finally if will call the `generate_pdf`
        method from the controller so this method returns the directory and file name of the pdf
        and returns the final `.pdf` to the client.

        Args:
            str_size: Size of the page.
            qr_data: Data to be added in the QR code.
            int_pages: Number of pages to be created.

        Returns:
            `flask_restful.abort` or `flask.send_from_directory`
        """
        # pylint: disable=E1111
        if str_size == "A4" or "letter":
            qr_len = len(qr_data)

            if qr_len > 4:
                pdf_file, pdf_directory = controller.generate_pdf(
                    str_size, qr_data, int_pages
                )

                api_return = flask.send_from_directory(
                    pdf_directory, pdf_file, as_attachment=True
                )
            else:
                api_return = flask_restful.abort(
                    404, error_message="QR data length should be higher than 4."
                )

        else:
            api_return = flask_restful.abort(404, error_message="Please check size.")
        # pylint: enable=E1111

        return api_return
