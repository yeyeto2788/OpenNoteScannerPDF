# OpenNoteScanner PDF Creator:

![Master build status](https://travis-ci.com/yeyeto2788/OpenNoteScannerPDF.svg?branch=master)

This repository contains some Python scripts that will let you create a final `.pdf` file to use with the Android Application OpenNoteScanner.

You can create the file by web API or by a single script. You go to [PythonAnywhere](http://yeyeto2788.pythonanywhere.com/) and you'll see the web
application running and get you `.pdf` file from it.  

<div style="text-align:center">
<img src="Doc/img/web_application.gif" width="350"/>
</div>

---
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [OpenNoteScanner PDF Creator:](#opennotescanner-pdf-creator)
	- [Quick explanation of the code:](#quick-explanation-of-the-code)
		- [Main PDF Generator script](#main-pdf-generator-script)
		- [Server application script](#server-application-script)
		- [API server script](#api-server-script)
	- [How to run the code through CLI in Linux:](#how-to-run-the-code-through-cli-in-linux)
	- [How to run the code for the server in Linux:](#how-to-run-the-code-for-the-server-in-linux)
	- [Final PDF example](#final-pdf-example)
	- [Android Application](#android-application)
	- [Some useful links:](#some-useful-links)
	- [Modules Documentation:](#modules-documentation)

<!-- /TOC -->

---
## Quick explanation of the code:

### Main PDF Generator script
With a given QR data, `.pdf` file name and a maximum amount of pages, it will create QR images of 512x512 Pixels with the QR data given plus a number ant the end of the data.

Once the QR images are generated the background images are created, these Background images are generated as:
 * 1 main background (white)
 * 1 middle image (black)
 * 1 top image (white).

Those images are pasted together to have a final image with a "Black Border" with an `A4` or `letter` size with a resolution of 300dpi.

Once all images are done, it will iterate over each QR image generated previously creating each page of the `.pdf` placing the QR images on the right bottom site of the page.

If you want more deep information please have a look at the auto generated documentation [here](./Doc/project_documentation/open_note_scanner).

### Server application script

This server application is developed with Flask framework and it just have only 1 landing page (`index.html`) with some information about how to use the API and some other info.

### API server script

The API is pretty straight forward, it only have one endpoint which is in `/api/<page_size>/<qr_data>/<int_pages>` so an example will be something like `/api/A4/P01_V05_S/50`
and the API will return a `.pdf` file generated using the main pdf generator script with the following information:
 * **PDF size** = A4
 * **QR data** = Images from `P01_V05_S-0000000` to `P01_V05_S-0000050`
 * **Number of pages** = `50`



## How to run the code through CLI in Linux:

  1. **Let's update our system:**

     ```
     sudo apt-get update
     sudo apt-get upgrade
     ```

  2. **Let's install the modules needed:**

      We actually need some modules but some of them depend on other modules so for this I have upload a file called **`requirement.txt`** which has all packages installed on my computer but you don't need all this modules on you computer, so you have two options to install the packages.

       * Option 1:
       ```
       sudo pip install Pillow
       sudo pip install reportlab
       sudo pip install qrcode
       ```
       * Option 2:
       ```
       sudo pip install -r requirement.txt
       ```

  3. **Let's test the code and the modules**

      let's go to the **`Test`** directory and let's execute one of the files.
      Execute this on the terminal: **`python Multiple_QRcodes.py`** or **`python Single_QRcode.py`**

  4. **We are ready to run the script and get the PDF file**

      Run the code by typing on the terminal the following command: **`python generate_single_pdf.py`** or **`sudo python generate_single_pdf.py`**
      This will generate the **`.pdf`** file on the **`PDF`** directory and the final images used on the  `.pdf` file in the **`QR`** directory.

## How to run the code for the server in Linux:

  1. **Follow steps for CLI operations first to that code is working properly**

  2. **So now let's just run the server**

      Run the server by the following command: **`python run_server.py`** or **`sudo python run_server.py`**

      Now we can open up a browser tab or window and go to the `127.0.0.1:800/api/<page_size>/<qr_data>/<int_pages>` where:
        * **page_size** = Should be either `A4` or `letter`

          If not the application will return the message **`Please check size.`**

        * **qr_data** = The data you want to have on the QR image

          You have to have a data length higher than 4 character because if you do not do it you'll get the error **`QR data length should be higher than 4.`**

        * **int_pages** = Integer with the numbers of the pages you want the `.pdf` file to have.

      This will be pages of the server:
        <div style="text-align:center">
          <img src="./Doc/img/pdf_embbeded_browser.png" alt="Image of the pdf embbeded on the browser"/>
          <img src="./Doc/img/pdf_embbeded_browser.png" alt="Image of the pdf embbeded on the browser"/>
        </div>

  3. **Print it!**

      If you followed the steps above you should have gotten the pdf file on the browser like this:

      <div style="text-align:center">
        <img src="./Doc/img/full_page_index.png" alt="Image of the server with index page" width="300"/>
        <img src="./Doc/img/full_page_documentation.png" alt="Image of the server with documentation page" width="300"/>
      </div>

      now you just have to print it.

  **Note:** If you want the server running on the background just and an ampersand (`&`) at the end of the command when you execute the server.


## Final PDF example
If you did it correctly you should get a `.pdf` file like this:

<div style="text-align:center">
  <img src="./Doc/img/pdf_image.png" alt="Image of the pdf file"/>
  <p>In this <a href="./Doc/pdf/Final.pdf"><b>link</b></a> you can see the final .pdf file created.</p>
</div>



## Android Application

[Google Play link](https://play.google.com/store/apps/details?id=com.todobom.opennotescanner&utm_source=global_co&utm_medium=prtnr&utm_content=Mar2515&utm_campaign=PartBadge&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1)

[GitHub Repository](https://github.com/ctodobom/OpenNoteScanner)

## Some useful links:

[Reporlab Module](https://pypi.python.org/pypi/reportlab/2.7).

[QRcode Module](https://pypi.python.org/pypi/qrcode/2.7).

[Pillow Module](https://pypi.python.org/pypi/Pillow/2.7.0).

[@BlackrockDigital](https://github.com/BlackrockDigital/startbootstrap-scrolling-nav) BootStrap template.


## Modules Documentation:

[Pillow Documentation](http://pillow.readthedocs.io/en/3.0.x/installation.html).

[Reportlab Documentation](https://www.reportlab.com/docs/reportlab-userguide.pdf).

[QRcode Documentation](https://github.com/lincolnloop/python-qrcode).
