#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Wenbin Fei, Email: wenbinfei@gmail.com
# All rights reserved.

"""
Have fun with Markdwon.
=======================
"""
import logging.config
import time
import traceback

# Create logger
import logger_ini
logger = logger_ini.logger_run()

####################################
# generate the Table of Content for Markdown
def toc(inFile, outFile=False, to_print=True):
    """
    Generate the Table of Content for Markdown
    todo: not generating the heading according to the comments # in codes
    using the following online tool:
    https://ecotrust-canada.github.io/markdown-toc/

    :type input_file: string
    :param input_file: the directory of the input markdown

    :type output_file: string or boolean
    :param output_file: if not false, the directory of the output markdown

    :type to_print: boolean
    :param to_print: the default is True to print on the screen
    """
    start_time = time.time()
    try: 
        mdFile = open(inFile, 'r')
        toc = []
        levels = [0,0,0,0]
        if isinstance(outFile, str) == True:
            newFile = open(outFile, 'w')
        tempFile = []
        tocLoc = 0
        partOfToc = False
        
        for line in mdFile:
            if partOfToc and line != '\n':
                continue
            else:
                partOfToc = False
            if 'Table of Contents' in line:
                tocLoc = len(tempFile) + 1
                partOfToc = True
            elif line[0] == '#':
                secId = buildToc(line, toc, levels)
                line = addSectionTag(cleanLine(line), secId) + '\n'
            tempFile.append(line)

        for line in toc:
            tempFile.insert(tocLoc, line)
            tocLoc += 1
            if to_print == True:
                print(line.rstrip('\n'))

        for line in tempFile:
            if isinstance(outFile, str) == True:
                newFile.write(line)
            
        mdFile.close()
        if isinstance(outFile, str) == True:            
            newFile.close()
    except: 
        logger.error('[toc failed]')
        logger.error(traceback.format_exc())        
        raise
    else: 
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"[toc completed] {inFile} in {round(dt,4)} s")

def addSectionTag(line, secId):
    startIndex = line.find(' ')
    line = line[:startIndex + 1] + '<a id=\'' + secId + '\' />' + line[startIndex + 1:]
    return line

def buildToc(line, toc, levels):
    line = cleanLine(line)
    secId = 's'
    if line[:4] == '####':
        raise UserWarning('Header levels greater than 3 not supported')
    elif line[:3] == '###':
        levels[3] += 1
        secId += str(levels[1]) + '-' + str(levels[2]) + '-' + str(levels[3])
        toc.append('      * [' + line[4:] + '](#' + secId + ')\n')
    elif line[:2] == '##':
        levels[2] += 1
        levels[3] = 0
        secId += str(levels[1]) + '-' + str(levels[2])
        toc.append('  * [' + line[3:] + '](#' + secId + ')\n')
    elif line[:1] == '#':
        levels[1] += 1
        levels[3] = levels[2] = 0
        secId += str(levels[1])
        toc.append('* [' + line[2:] + '](#' + secId + ')\n')
    return secId

def cleanLine(text):
    text = stripNewline(text)
    text = removeAnchors(text)
    return text

def stripNewline(text):
    return text.replace('\n', '')

def removeAnchors(text):
    while ('<' in text and '>' in text):
        leftTag = text.index('<')
        rightTag = text.index('>')
        text = text[0:leftTag] + text[rightTag + 1:]
    return text
####################################################

if __name__ == "__main__":
    import sys
    # toc('../README.md', False, True)
    toc(r"C:\Wenbin\GitHub\Lynx\docs\Image-processing_notes.md", False, True)
    


