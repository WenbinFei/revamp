# Revamp - A collection of methods for file management
*Author: Wenbin Fei  
Email:	 wenbinfei@gmail.com  
System:  Ubuntu  
Language: Bash & Python3*

* [Revamp - A collection of methods for file management](#s1)
  * [File Management on Operating System](#s1-1)
  * [PDF](#s1-2)
      * [PDF compress](#s1-2-1)
      * [PDF Decryption](#s1-2-2)
  * [Markdown](#s1-3)
      * [Table of content generator](#s1-3-1)


## File Management on Operating System
### Copy filter: copy files with certern extentions
Use bash command rsync
The bash commad can also be used directly on the termnial by typing or create a .sh file.
```
rsync -a --include '*/' --include '*.<file_extension_1>' --include '*.file_extension_2' --include '*.file_extension_3' --exclude '*' <source_folder> <target_folder>
```
### Batch rename file and folder
it supoorts to rename files with a certain extension in a folder

## PDF 
### PDF compress
*If you do not worry about safety, you can do the PDF compression on the website [PDF Compressor](https://pdfcompressor.com/)*

[Ghostscript](https://www.ghostscript.com/doc/current/Use.htm) command on terminal.

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

### PDF Decryption
Using a python library *pikepdf* for the decryption
You can run the follwoing command directly on the 

## Markdown 
### Table of content (ToC) generator
- Option 1: Run the following bash command will only print the ToC on the termainal
- Run the following bash command will only print the ToC and generate a new markdwon file with the ToC  
- Alternatively, you can use the website [GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/) to generate the Table of Content