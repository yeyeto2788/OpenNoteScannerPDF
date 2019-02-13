## NAME
utils

## FUNCTIONS

### `create_directory()`
This function will check whether directory to create image exist or not.

If it does not exit it will generate the directory.

**Returns:** Always True, take into account that if directory does not exists it will create it.


### `debug(*args, **kargs)`
wrapper to print values on the terminal in case debug mode is enable.

**Args:**

 * **`*args`**  Arguments for the print function.
 * **`**kargs`**  Keyword arguments to the print function.


### `delete_images(bln_delete=0)`
Delete images after PDF is created if argument is passed.

**Args:**

 * **`bln_delete`**  whether do or not the operation.


### `delete_pdfs(bln_delete=0)`
Delete pdf if argument is passed.

**Args:**

 * **`bln_delete`**  whether do or not the operation.

## DATA
BASE_PATH = Module directory.

PDF_DIR = PDF directory.

QR_DIR = Images directory.

