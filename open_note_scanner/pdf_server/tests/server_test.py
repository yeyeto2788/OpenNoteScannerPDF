import logging
import unittest

from open_note_scanner.pdf_server.server import app


class TestAppEndPoints(unittest.TestCase):
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
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        self.app_views = [
            rule.__str__()
            for rule in app.url_map._rules
            if "GET" in rule.methods
            and (
                not rule.__str__().endswith("/<int:int_pages>")
                and not rule.__str__().endswith("/<path:filename>")
            )
        ]

        self.app = app.test_client()

    def test_root(self):
        """
        Check whether the root path is enable.

        """
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(
            response.status_code,
            200,
            msg="Expected: {}, Obtained: {}".format(200, response.status_code),
        )

    def test_get_routes(self):
        """
        Test to check whether all `GET` endpoints are fully working.

        """
        for route in self.app_views:
            response = self.app.get(route, follow_redirects=True)
            self.assertEqual(
                response.status_code,
                200,
                msg="Expected: {}, Obtained: {}".format(200, response.status_code),
            )

    def tearDown(self):
        """
        Test tearDown.
        """

    @classmethod
    def tearDownClass(cls):
        """
        Global tearDown.
        """
