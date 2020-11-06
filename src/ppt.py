#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Wenbin Fei, Email: wenbinfei@gmail.com
# All rights reserved.

"""
Have fun with PowpwerPoint files.
todo: the strange thinng is when the powerpoint is open.
but when run the smae code on the shell, it works.
"""

import os
import win32com.client
import logging.config
import time
import traceback

# Create logger
logging.config.fileConfig(fname='logging.ini')
logger = logging.getLogger(__name__)

import image

def ppt2tif(ppt_path, crop = True, long_image = False ):
    """
    Save PPT as tif in foler individual_figures for journal papers, and crop the top and bottom margin out.
    The individual figures also can be combined into one long figure.

    :type ppt_path: string
    :para ppt_path: the directory of the PPT file. NOTE: The relative path does not work

    :type crop: boolean
    :para crop: the default is True to crop the figures exported from PPT

    :type long_image: Boolean
    :para long_image: the default is False 

    """
    start_time = time.time()
    try: 
        ppt_app = win32com.client.Dispatch('PowerPoint.Application')
        ppt_app.Visible = True # show the powerpoint software
        ppt = ppt_app.Presentations.Open(ppt_path)  # open PPT  
        output_path = os.path.split(ppt_path)[0] + '/individual'    # the figures will be stored in individual folder
        print(output_path)       
        ppt.SaveAs(output_path, 17)  # 17 is the id of jpg, 
        ppt_app.Quit() 
    except: 
        logger.error(traceback.format_exc())
        logger.error('ppt has not been opened correctly')
        raise
    else: 
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"[ppt2tif completed] {ppt_path} in {dt} s")

        if long_image:
            image.generate_long_image(output_path)  



if __name__ == '__main__':
    ppt2tif(r"C:/Wenbin/GitHub/revamp/tests/in.pptx")