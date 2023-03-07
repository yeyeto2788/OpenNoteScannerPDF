from itertools import permutations
from unittest import TestCase
from unittest import mock

from open_note_scanner import utils


def simple_join(first_string: str, second_string: str) -> str:
    """
    Simple function to simulate a join of a string in order to
    mock as side effect a `os.join` module.
    Args:
        first_string:
        second_string:

    Returns:
        String joined.
    """

    return first_string + second_string


class UtilsTest(TestCase):
    def setUp(self) -> None:
        self.thread_id = 15864
        self.pdf_dir = "/some/path/to/pdfs/folder"
        self.qr_dir = "/some/path/to/qr/folder"
        self.image_list = ["image1.png", "image20.png", "image30.png", "image40.png"]
        self.pdf_list = ["dummy1.pdf", "dummy10.pdf", "dummy2.pdf", "dummy5.pdf"]

        self.patches = [
            mock.patch("open_note_scanner.utils.os"),
            mock.patch("open_note_scanner.utils.PDF_DIR"),
            mock.patch("open_note_scanner.utils.QR_DIR"),
            mock.patch("open_note_scanner.utils.debug"),
        ]

        for mocked_item in self.patches:
            mocked_item.start()

        self.patches[0].get_original()[0].path.join.side_effect = simple_join
        self.patches[0].get_original()[0].makedirs.return_value = True
        self.patches[0].get_original()[0].path.exists.return_value = True
        self.patches[0].get_original()[0].remove.return_value = True
        # Assign a different value to the utils constant
        self.patches[1].get_original()[0].return_value = self.pdf_dir
        self.patches[2].get_original()[0].return_value = self.qr_dir

    def test_create_directory(self):
        """
        Check that the `utils.create_directory` function work as expected.
        """

        obtained = utils.create_directory(self.thread_id)

        self.assertTrue(obtained, msg=f"Expected: {True}, Obtained: {obtained}")
        self.patches[3].get_original()[0].assert_called()

    def test_create_directory_abnormal(self):
        """
        Check that the `utils.create_directory` function work as expected.
        """

        # Mock all side effects and return values for the os.path module.
        self.patches[0].get_original()[0].path.exists.return_value = False

        obtained = utils.create_directory(self.thread_id)

        self.assertTrue(obtained, msg=f"Expected: {True}, Obtained: {obtained}")
        self.patches[3].get_original()[0].assert_called()

    def test_delete_images(self):
        """
        Check that the `utils.delete_images` function work as expected.
        """

        # Mock all side effects and return values for the os.path module.
        self.patches[0].get_original()[
            0
        ].path.abspath.return_value = f"{self.qr_dir}/{str(self.thread_id)}"
        self.patches[0].get_original()[0].listdir.return_value = self.image_list

        utils.delete_images(self.thread_id, True)

        self.patches[0].get_original()[0].remove.assert_called()

    def test_delete_images_abnormal(self):
        """
        Check that the `utils.delete_images` function work as expected.
        """

        # Mock all side effects and return values for the os.path module.
        self.patches[0].get_original()[
            0
        ].path.abspath.return_value = f"{self.qr_dir}/{str(self.thread_id)}"
        self.patches[0].get_original()[0].path.exists.return_value = False

        utils.delete_images(self.thread_id, True)

        self.patches[0].get_original()[0].remove.assert_not_called()

    def test_delete_pdfs(self):
        """
        Check that the `utils.delete_pdfs` function work as expected.
        """

        # Mock all side effects and return values for the os.path module.
        self.patches[0].get_original()[0].listdir.return_value = self.pdf_list
        self.patches[0].get_original()[
            0
        ].path.abspath.return_value = f"{self.pdf_dir}/{str(self.thread_id)}"

        try:
            utils.delete_pdfs(self.thread_id, bln_delete=True)

        except Exception:
            self.fail(
                msg="The method `utils.delete_pdfs` should have raised an exception."
            )

    def test_delete_pdfs_abnormal(self):
        """
        Check that the `utils.delete_pdfs` function work as expected.
        """

        # Mock all side effects and return values for the os.path module.
        self.patches[0].get_original()[0].path.exists.return_value = False
        self.patches[0].get_original()[
            0
        ].path.abspath.return_value = f"{self.pdf_dir}/{str(self.thread_id)}"

        try:
            utils.delete_pdfs(self.thread_id, bln_delete=True)

        except Exception:
            self.fail(
                msg="The method `utils.delete_pdfs` should have raised an exception."
            )

    def test_sort_alphanumeric_list(self):
        """
        Check that the `utils.sort_alphanumeric_list` function work as expected.
        """

        expected = ["aaa", "ahola1", "bba", "hola", "hola1", "hola2"]

        for unsorted_list in permutations(
            ["hola1", "hola2", "ahola1", "hola", "aaa", "bba"]
        ):
            obtained = utils.sort_alphanumeric_list(list(unsorted_list))
            self.assertEqual(
                expected, obtained, msg=f"Expected: {expected}, Obtained: {obtained}"
            )
