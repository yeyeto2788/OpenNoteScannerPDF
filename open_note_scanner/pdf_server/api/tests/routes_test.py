import logging

from unittest import TestCase, mock

from open_note_scanner.pdf_server.server import app


class TestAppEndPoints(TestCase):
    """
    Unitary tests for utils.
    """

    @classmethod
    def setUpClass(cls):
        """
        Global setUp.
        """

        logging.basicConfig(level=logging.INFO)

    def setUp(self):
        """
        Test setUp.
        """
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app_views = [
            rule.__str__() for rule in app.url_map._rules if 'GET' in rule.methods and (
                    not rule.__str__().endswith(
                        '/<int:int_pages>') and not rule.__str__().endswith('/<path:filename>'))
        ]

        self.app = app.test_client()

        self._patches = [
            mock.patch("open_note_scanner.pdf_generator.generator.PDFGenerator"),
            mock.patch("open_note_scanner.pdf_generator.generator.os"),
            mock.patch("open_note_scanner.utils.os"),
        ]

        for patch in self._patches:
            patch.start()

    @mock.patch(
        'open_note_scanner.pdf_server.api.controller.generate_pdf'
    )
    def test_valid_urls(self, mock_generate_pdfs):
        """
        Check whether the api returns the pdf and no error is raised when passing correct values.

        """
        mock_generate_pdfs.return_value = ('/some/route/to/pdf', 'dummy.pdf')

        self._patches[1].get_original()[0].remove.return_value = True
        self._patches[1].get_original()[0].chdir.return_value = True
        self._patches[1].get_original()[0].abspath.return_value = "dummy.pdf"

        paper_sizes = ['A4', 'letter']
        qr_data = ['{}{:03}'.format(size, index) for index, size in enumerate(paper_sizes)]
        int_pages = ['10', '25']

        urls = ['/'.join(x) for x in list(zip(paper_sizes, qr_data, int_pages))]
        print(urls)

        with mock.patch('flask.send_from_directory') as mocked:
            mocked.return_value = True

            for url in urls:
                api_url = '/api/{}'.format(url)
                response = self.app.get(api_url, follow_redirects=True)
                self.assertEqual(response.status_code, 200,
                                 msg="Expected: {}, Obtained: {} trying to get {}".format(
                                     200, response.status_code, api_url))

    @mock.patch(
        'open_note_scanner.pdf_server.api.controller.generate_pdf'
    )
    def test_invalid_values(self, mock_generate_pdfs):
        """
        Check whether the api returns the pdf and an error is raised when passing incorrect values.

        """
        mock_generate_pdfs.return_value = ('/some/route/to/pdf', 'dummy.pdf')

        self._patches[1].get_original()[0].remove.return_value = True
        self._patches[1].get_original()[0].chdir.return_value = True
        self._patches[1].get_original()[0].abspath.return_value = "dummy.pdf"

        paper_sizes = ['NO_SIZE']
        qr_data = ['{}{:03}'.format(size, index) for index, size in enumerate(paper_sizes)]
        int_pages = ['10', '25']

        urls = ['/'.join(x) for x in list(zip(paper_sizes, qr_data, int_pages))]
        print(urls)

        for url in urls:
            api_url = '/api/{}'.format(url)
            response = self.app.get(api_url, follow_redirects=True)
            self.assertEqual(
                response.status_code,
                404,
                msg=f"Expected: {404}, Obtained: {response.status_code} trying to get {api_url}"
            )

        mock_generate_pdfs.asser_not_called()

    def test_invalid_urls(self):
        """
        Check whether the api returns the error when passing incorrect values.

        """
        paper_sizes = ['A4', 'letter']
        qr_data = ['{}{}'.format(size[:1], index) for index, size in enumerate(paper_sizes)]
        int_pages = ['10', '25']

        urls = ['/'.join(x) for x in list(zip(paper_sizes, qr_data, int_pages))]
        print(urls)

        for url in urls:
            api_url = '/api/{}'.format(url)
            response = self.app.get(api_url, follow_redirects=True)
            self.assertEqual(response.status_code, 404,
                             msg="Expected: {}, Obtained: {} trying to get {}".format(
                                 404, response.status_code, api_url))

    def tearDown(self):
        """
        Test tearDown.
        """

    @classmethod
    def tearDownClass(cls):
        """
        Global tearDown.
        """
