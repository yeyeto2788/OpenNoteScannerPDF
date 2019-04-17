"""

Common operations to be used all over the module.

"""
import os
import re

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
QR_DIR = os.path.join(BASE_PATH, "QR")
PDF_DIR = os.path.join(BASE_PATH, "PDF")


def create_directory():
    """
    This function will check whether directory to create image exist or not.

    If it does not exit it will generate the directory.

    Returns:
        Always True, take into account that if directory does not exists it will create it.
    """

    for str_directory in [QR_DIR, PDF_DIR]:

        if os.path.exists(str_directory):
            debug("No need to create directory")
            bln_return = True
        else:
            os.mkdir(str_directory)
            debug("Directory created {}".format(str_directory))
            bln_return = True

    return bln_return


def delete_images(bln_delete=0):
    """
    Delete images after PDF is created if argument is passed.

    Args:
        bln_delete: whether do or not the operation.

    """
    if bln_delete and os.path.exists(QR_DIR):
        images = os.listdir(QR_DIR)
        if images:

            for image in images:
                if image.endswith(".png"):
                    os.remove(os.path.join(QR_DIR, image))


def delete_pdfs(bln_delete=0):
    """
    Delete pdf if argument is passed.

    Args:
        bln_delete: whether do or not the operation.

    """

    if bln_delete and os.path.exists(PDF_DIR):
        files = os.listdir(PDF_DIR)

        if files:
            for pdf in files:
                remove_pdf = os.path.join(PDF_DIR, pdf)

                if remove_pdf.endswith(".pdf") and os.path.exists(remove_pdf):
                    os.remove(remove_pdf)


def debug(*args, **kargs):
    """
    wrapper to print values on the terminal in case debug mode is enable.

    Args:
        *args: Arguments for the print function.
        **kargs: Keyword arguments to the print function.

    """

    bln_print = 0

    if bln_print:
        print(*args, **kargs)


def sort_alphanumeric_list(lst_unsorted):
    """
    Sorts the given iterable in the way that is expected.

    Args:
        lst_unsorted: List of values to be sorted.

    Returns:
        Same list sorted.

    """

    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(lst_unsorted, key=alphanum_key)
