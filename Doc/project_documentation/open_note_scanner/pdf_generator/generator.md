## NAME
generator

## CLASSES
builtins.object
PDFGenerator


### `class PDFGenerator(builtins.object)`

### `PDFGenerator(str_qr_data, pdf_name, int_pages)`

Class object to call different functions to create the images needed to
generate the PDF files.

Methods defined here:


### `__init__(self, str_qr_data, pdf_name, int_pages)`
Constructor method to have the variables in the class

**Args:**

 * **`str_qr_data`**  Data that the qr code will contain.
 * **`pdf_name`**  Name of the pdf file.
 * **`int_pages`**  Number of pages that pdf will have.


### `create_images(self)`
This function will generate .png images with a string data replacing
last characters of the string by the number of iteration in order to
have a uniques QR codes and names.


### `generate_pdf(self, size='A4', bln_delete=1)`
Create the PDF based on the images in QR directory.

**Args:**

 * **`size`**  size of the paper.
 * **`bln_delete`**  boolean to delete or not previous runs.

**Returns:** String with the directory where the `.pdf` was created.


## DATA
A4 = (595.2755905511812, 841.8897637795277)

SIZES = {'A4': (595.2755905511812, 841.8897637795277), 'letter': (612.0, 792.0)}

inch = 72.0

letter = (612.0, 792.0)
