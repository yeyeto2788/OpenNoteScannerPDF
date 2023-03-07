"""

PDF generator for the OpenNoteScanner Android application,
this module is in charge of holding all logic of the generation of the pdf
file.

"""

from open_note_scanner.pdf_generator.generator import SIZES
from open_note_scanner.pdf_generator.generator import PDFGenerator

VERSION_INFO = {
    "MAJOR": 0,
    "MINOR": 0,
    "PATCH": 1,
}
__version__ = "{MAJOR:d}.{MINOR:d}.{PATCH:d}".format(**VERSION_INFO)
__author__ = "Juan Biondi"
__email__ = "juanernestobiondi@gmail.com"
__maintainer__ = "Juan Biondi"

__status__ = "Development"
