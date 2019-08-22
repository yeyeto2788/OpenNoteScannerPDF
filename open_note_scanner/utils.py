"""

Common operations to be used all over the module.

"""
import os
import re

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp'))
TEMP_PATH = os.getenv("TEMP_DIR", BASE_PATH)
QR_DIR = os.path.join(TEMP_PATH, "QR")
PDF_DIR = os.path.join(TEMP_PATH, "PDF")


def create_directory(thread_id: int):
    """
    This function will check whether directory to create image exist or not.

    If it does not exit it will generate the directory.

    Args:
        thread_id:

    Returns:
        Always True, take into account that if directory does not exists it will create it.
    """

    for str_directory in [QR_DIR, PDF_DIR]:

        if os.path.exists(os.path.join(str_directory, str(thread_id))):
            debug("No need to create directory")
            bln_return = True

        else:
            os.makedirs(os.path.join(str_directory, str(thread_id)))
            debug("Directory created {}".format(os.path.join(str_directory, str(thread_id))))
            bln_return = True

    return bln_return


def delete_images(thread_id: int, bln_delete: bool = False):
    """
    Delete images after PDF is created if argument is passed.

    Args:
        thread_id:
        bln_delete: whether do or not the operation.

    """
    qr_directory = os.path.abspath(os.path.join(QR_DIR, str(thread_id)))

    if bln_delete and os.path.exists(qr_directory):
        images = os.listdir(qr_directory)

        if images:

            for image in images:

                if image.endswith(".png"):
                    os.remove(os.path.join(qr_directory, image))


def delete_pdfs(thread_id: int, bln_delete: bool = False):
    """
    Delete pdf if argument is passed.

    Args:
        thread_id:
        bln_delete: whether do or not the operation.

    """

    pdf_directory = os.path.abspath(os.path.join(PDF_DIR, str(thread_id)))

    if bln_delete and os.path.exists(pdf_directory):
        files = os.listdir(pdf_directory)

        if files:

            for pdf in files:
                remove_pdf = os.path.join(pdf_directory, pdf)

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
