# Revamp - A collection of methods for file management
*Author: Wenbin Fei  
Email:	 wenbinfei@gmail.com  
System:  Ubuntu  
Language: Bash & Python3*

## File Management on Operating System


## PDF
### PDF compress
*If you do not worry about safety, you can do the PDF compression on the website [PDF Compressor](https://pdfcompressor.com/)*

**Method**: [Ghostscript](https://www.ghostscript.com/doc/current/Use.htm) command on terminal.

Step 1: Install Ghostscript by typing the following command on terminal.
```
sudo apt update
sudo apt install ghostscript
```
Step 2: Using the following command on terminal
```
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
-dNOPAUSE -dBATCH -dColorImageResolution=150 \
-sOutputFile=output.pdf someBigFile.pdf
```

### PDF Decryption
**Method"**: Using a python library: pikepdf

Step 1: Install pikepdf by typing the following command on terminal.
```
pip install pikepdf
```
Step 2: Using the following python codes
```
import pikepdf

pdf = pikepdf.open('unextractable.pdf')
pdf.save('extractable.pdf')
```
