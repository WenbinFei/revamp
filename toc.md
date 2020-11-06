* [Revamp - A collection of methods for file management](#s1)
  * [File Management on Operating System](#s1-1)
  * [PDF](#s1-2)
      * [PDF compress](#s1-2-1)
      * [PDF Decryption](#s1-2-2)
  * [Markdown](#s1-3)
      * [Table of content generator](#s1-3-1)
# <a id='s1' />Revamp - A collection of methods for file management
*Author: Wenbin Fei  
Email:	 wenbinfei@gmail.com  
System:  Ubuntu  
Language: Bash & Python3*

- [File Management on Operating System](#file-management-on-operating-system)
- [PDF](#pdf)
  * [PDF compress](#pdf-compress)
  * [PDF Decryption](#pdf-decryption)
 - [Markdown]



## <a id='s1-1' />File Management on Operating System


## <a id='s1-2' />PDF
### <a id='s1-2-1' />PDF compress
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
-sOutputFile=output.pdf input.pdf
```

### <a id='s1-2-2' />PDF Decryption
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
## <a id='s1-3' />Markdown
### <a id='s1-3-1' />Table of content generator
We use the website [GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/) to generate the Table of Content