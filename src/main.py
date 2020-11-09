#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Wenbin Fei, Email: wenbinfei@gmail.com
# All rights reserved.

"""
Run Revamp - software for file management and dealing with files
================================================================
"""
import os
import logging.config
import time
import traceback


#### Template ################################
##### Crop all figures in a folder for journal papers ##########
def crop_all_fig_in_folder (input_dir):
	"""
	Crop all figures in a folder for journal papers

	:type input_dir: string
    :param input_dir: the directory of the folder iamges 
	"""
	
	from image import crop_journal_image as imcj

	path_list = os.listdir(input_dir)
	for term in path_list:
		image_path = input_dir + '/' + term
		imcj(image_path) 

def replace_original_image(input_dir, marker):
	"""
	Replace the original image with cropped images

	:type input_dir: string
    :param input_dir: the directory of the folder iamges 

    :type marker: string
    :param marker: put some markers like '_cropped' or '_resized'  
	"""
	path_list = os.listdir(input_dir)
	for term in path_list:
		if marker in term:
			original_file = term.replace(marker,'')
			image_path = input_dir + '/' + term
			image_path_orig = input_dir + '/' + original_file
			os.remove(image_path_orig)
			os.rename(image_path, image_path_orig)			

# to crop figures and replace the original figures			
input_dir = r"C:\Wenbin\GitHub\revamp\tests\individual"
crop_all_fig_in_folder(input_dir)
# replace_original_image(input_dir, '_cropped')





#### Pdf decrypte ############################
# import pdf
# pdf.decrypte('../tests/in.pdf', '../tests/out.pdf')

#### Test ####################################	
##### Test ppt.py #############################
## todo: the strange thinng is when the powerpoint is open.
## but when run the smae code on the shell, it works.
# import ppt
# ppt.ppt2tif(r"C:/Wenbin/GitHub/revamp/tests/in.pptx", True, True)


