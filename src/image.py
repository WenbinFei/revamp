#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Wenbin Fei, Email: wenbinfei@gmail.com
# All rights reserved.

"""
Have fun with images.
"""

import os
import logging.config
import time
import traceback
import numpy as np
import cv2

# Create logger
logging.config.fileConfig(fname='logging.ini')
logger = logging.getLogger(__name__)

def crop_journal_image(path):
    """
    Crop the images generated by PPT acrrosing one column or two columns in the journal Export a cropped image with name fig_crpped.XXX

    :type path: string
    :param path: the directory of the iamges 
    """
    start_time = time.time()
    try: 
        store_row = []
        img = cv2.imread(path)    
        for i in range(img.shape[0]):
            img_row = img[i]
            if(np.any(img_row<255)):
                store_row.append(i)

        # check whether the image only occupies one-column in the journal  
        check_1_col = img[store_row[0]] 
        column_num = img.shape[1] # only use one row to check to save time
        img_row_spl = np.hsplit(check_1_col, [column_num//2]) # only check only part
        img_row_left = np.all(img_row_spl[0] == 255) # whether the left part is empty
        img_row_right = np.all(img_row_spl[1] == 255) # whether the right part is empty
        if(img_row_right):
            store_col = range(column_num//2 + 1) # only keep the index of the left part
        elif(img_row_left):
            store_col = range(column_num//2, icolumn_num) # only keep the index of the right part
        else:
            store_col = ':' # keep the whole line
        crop_img = img[store_row][:, store_col]
    except: 
        logger.error('[crop_journal_image failed]')
        logger.error(traceback.format_exc())        
        raise
    else: 
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"[crop_journal_image completed] {path} in {dt} s")
        
        # cv2.imshow('cropped', crop_img)
        # cv2.waitKey(0) 

        # the cropped file with exported with a tailed _cropped afte the original name
        path_split = path.rsplit('.', 1)    
        output_path = path_split[0] + '_croped.' +   path_split[-1]    
        cv2.imwrite(output_path, crop_img)

def resize_image(path, percentage):
    """
    Resize an image according to the percentage using python opencv.
    A new image will be generated with _resized.XX    

    :type path: string
    :param path: the directory of the iamges 

    :type percentage: int
    :param percentage: the percent of the original image 
    """
    start_time = time.time()
    try:
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        width = int(img.shape[1] * percentage / 100)
        height = int(img.shape[0] * percentage / 100)
        dim = (width, height)
        resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    except: 
        logger.error('[resize_image failed]')
        logger.error(traceback.format_exc())        
        raise
    else: 
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"[resize_image completed] {path} in {dt} s")
        
        # cv2.imshow('cropped', crop_img)
        # cv2.waitKey(0) 

        # the cropped file with exported with a tailed _cropped afte the original name
        path_split = path.rsplit('.', 1)    
        output_path = path_split[0] + '_resized.' +   path_split[-1]    
        cv2.imwrite(output_path, resized_img)
     

def generate_long_image(output_path):
    """
    Generate long image by combing individual images

    :type output_path: string
    :param input_file: the directory of the iamges to be saved 
    """
    try:
        picture_path = output_path[:output_path.rfind('.')]
        last_dir = os.path.dirname(picture_path)  # parent directory

        # achevie individual images
        ims = [Image.open(os.path.join(picture_path, fn)) for fn in os.listdir(picture_path)]
        width, height = ims[0].size   
        long_canvas = Image.new(ims[1].mode, (width, height * len(ims))) #create n photos with the same width
    except: 
        logger.error(traceback.format_exc())
    else:
        # merge figures
        for i, image in enumerate(ims):
                long_canvas.paste(image, box=(0, i * height))

        long_canvas.save(os.path.join(last_dir, 'long-image.tif'))  # save as long figure
        logger.info(f"[generate_long_image completed]")


if __name__ == "__main__":
    # crop_journal_image(r"../tests/individual/Slide2.Tif")
    resize_image(r"../tests/individual/Slide2.Tif", 60)     