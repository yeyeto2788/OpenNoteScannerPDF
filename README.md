#OpenNoteScanner PDF Creator:
### This script will create a final PDF file to use with the Android Application OpenNoteScanner it is based on Python 2.7

####Quick explanation of the code:
With a given name for the images and for the final PDF, the code will itinerate based on a maximum amount of pages (~~right now it is hardcoded 50~~), it will create the QR images on a 512x512 Pixels, once the QR codes are generated the background images are created.

These Background images are created based on generating one main background (white) the middle image (black) and the top image (white). Those images are pasted together to have a page/image with a "Black Border" with a A4 size based on 300dpi.

Once all this is done will itinerate again on each QR code creating each page of the PDF pasting the codes on the right bottom site of the page.

Finally, we do a itineration on the images so we can append the images into a variable to generate the PDF file.

**Note:** 

* The images and the PDF are created on a separate directory called ```QR_Images```
* The name of the images should be at least 4 characters long.
* Somatimes depending on the OS you have to run the script as ```sudo``` or ```administrator```

#####**Steps to follow:**
1. **Let's update our system:**

 ```
 sudo apt-get update
 sudo apt-get upgrade
 ```

2. **Let's install the modules needed:**
We actually need some modules but some of them depend on other modules so for this I have upload a file called ```requirement.txt``` which has all packages installed on my computer but you don't need all this modules on you computer, so you have two options to install the packages.

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
let's go to the ```Test``` directory and let's execute one of the files.
```python Multiple_QRcodes.py``` or ```python Single_QRcode.py```

4. **We are ready to run the script and get the PDF file**
```python Generate_QRcodes_PDF.py```
This will generate the ```.pdf``` file on the ```QR_Images``` directory and the final images used on the  PDF file in ```.png``` 

**You should get files like this:**

![Final Images on the PDF](https://github.com/yeyeto2788/OpenNoteScannerPDF/blob/master/TestImage.png)

[Final PDF](https://github.com/yeyeto2788/OpenNoteScannerPDF/blob/master/QR_Images/Final.pdf)


####TO DO list:
[ ] Remove unnecessary code and variables on the script and directory.

[x] Remove unnecessary images.

[ ] Check if it works on other OS. 

[ ] Fork the code on OpenNoteScanner repository.

[ ] Better alignment of the images on the final PDF.

[ ] Investigate why the black border is not completely shown on the images.

[ ] Improve code to generate the pages as we expect (from 1 to maximum amount of pages).

[x] Create global variable for Maximum amount of pages.

[x] Improve documentation.



**Android Application**

[Google Play link](https://play.google.com/store/apps/details?id=com.todobom.opennotescanner&utm_source=global_co&utm_medium=prtnr&utm_content=Mar2515&utm_campaign=PartBadge&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1)

[GitHub Repository](https://github.com/ctodobom/OpenNoteScanner)

**Some useful links:**

[Reporlab Module](https://pypi.python.org/pypi/reportlab/2.7).

[QRcode Module](https://pypi.python.org/pypi/qrcode/2.7).

[Pillow Module](https://pypi.python.org/pypi/Pillow/2.7.0).


**Modules Documentation:**

[Pillow Documentation](http://pillow.readthedocs.io/en/3.0.x/installation.html).

[Reportlab Documentation](https://www.reportlab.com/docs/reportlab-userguide.pdf).

[QRcode Documentation](https://github.com/lincolnloop/python-qrcode).

