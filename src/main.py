#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Wenbin Fei, Email: wenbinfei@gmail.com
# All rights reserved.

"""
Run Revamp - software for file management and dealing with files
================================================================
"""
# import file_manage
import file_manager
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
		if term.endswith('.TIF'):
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
			# os.rename(image_path, image_path_orig)	

			new_name = original_file.replace('Slide','Fig')			
			new_name_path = input_dir + '/' + new_name
			os.rename(image_path, new_name_path)	




##### to crop figures and replace the original figures			
input_dir = r"C:\Users\wenbinf1\OneDrive - The University of Melbourne\WF_share_with_GAN\1_Journal-papers\1_shortest-path-heat\Figures\Figures - Individual Files"
crop_all_fig_in_folder(input_dir)
replace_original_image(input_dir, '_cropped')


##### Create dir_list.txt #################
# input_dirs = [line.strip() for line in open('C:/Users/wenbinf1/OneDrive - The University of Melbourne/WF_share_with_GAN/1_Journal-papers/2-stress-anisotropy/Data/2_network-features/dir_list_cases.txt','r')]

# for case in input_dirs:
# 	input_dir_x = case + '/network-feature/data-x'
# 	input_dir_y = case + '/network-feature/data-y'
# 	input_dir_z = case + '/network-feature/data-z'
# 	output_dir_x = input_dir_x + '/dir_list.txt'
# 	output_dir_y = input_dir_y + '/dir_list.txt'
# 	output_dir_z = input_dir_z + '/dir_list.txt'

# 	file_manager.dir_list(input_dir_x, output_dir_x, True)
# 	file_manager.dir_list(input_dir_y, output_dir_y, True)
# 	file_manager.dir_list(input_dir_z, output_dir_z, True)


#### Pdf decrypte ############################
# import pdf
# pdf.decrypte('../tests/in.pdf', '../tests/out.pdf')

#### Test ####################################	
##### Test ppt.py #############################
## todo: the strange thinng is when the powerpoint is open.
## but when run the smae code on the shell, it works.
# import ppt
# ppt.ppt2tif(r"C:/Wenbin/GitHub/revamp/tests/in.pptx", True, True)

#### Template ####
###### bath resize images ####
# input_dir = r"C:\Users\wenbinf1\OneDrive - The University of Melbourne\WF_share_with_GAN\2_Conference\Grain-days_2020\posters"
# path_list = os.listdir(input_dir)
# marker = '.png'
# for term in path_list:
# 	if marker in term:			
# 		image_path = input_dir + '/' + term
# 		image.resize_image(image_path,30)


