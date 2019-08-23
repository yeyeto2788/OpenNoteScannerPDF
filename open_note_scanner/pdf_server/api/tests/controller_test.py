from unittest import TestCase, mock

from open_note_scanner.pdf_server.api import controller


class ControllerTest(TestCase):

    def setUp(self):
        self._patches = [
            mock.patch('open_note_scanner.pdf_server.api.controller.pdf_generator.PDFGenerator'),
            mock.patch('open_note_scanner.pdf_server.api.controller.os'),
            mock.patch('open_note_scanner.utils.delete_pdfs'),
        ]

        for mocked_item in self._patches:
            mocked_item.start()

    def test_generate_pdf(self):
        """
        Check whether the `generate_pdf` method from the
        `open_note_scanner.pdf_server.api.controller` module works as expected.
        """

        size = 'A4'
        qr_data = 'Testing data'
        pages = 25
        pdf_route = 'crazy/route/to/pdf/great.pdf'
        # Mock the actual generation of the pdf file.
        self._patches[0].get_original()[0].return_value = mock.MagicMock()
        self._patches[0].get_original()[0].return_value.generate_pdf.return_value = pdf_route
        # Mock function calls to the os module.
        self._patches[1].get_original()[0].path.basename.return_value = pdf_route.split('/')[-1]
        self._patches[1].get_original()[0].path.dirname.return_value = '/'.join(
            pdf_route.split('/')[:-1]
        )
        # Mock the deletion of file.
        self._patches[2].get_original()[0].return_value = True

        filename, file_dir = controller.generate_pdf(size, qr_data, pages)

        self.assertEqual(
            pdf_route.split('/')[-1],
            filename,
            f"Expected: {pdf_route.split('/')[-1]}, Obtained: {filename}")

        self.assertEqual(
            '/'.join(pdf_route.split('/')[:-1]),
            file_dir,
            f"Expected: {'/'.join(pdf_route.split('/')[:-1])}, Obtained: {file_dir}")
