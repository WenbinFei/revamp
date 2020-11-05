#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Wenbin Fei, Email: wenbinfei@gmail.com
# All rights reserved.

"""
Deal with PDF files.
Todo: 
	1. to test function compress
	2. to test whether the log file works well on ubuntu
"""

import os
import logging.config
import time
import traceback

# Create logger
logging.config.fileConfig(fname='logging.ini')
logger = logging.getLogger(__name__)


# Create functions

def compress(input_file, output_file, resolution):
	"""
	Compress PDF using bash command of Ghostscript on terminal shell.
	Run the following bash command to install Ghostcript:
		sudo apt update
		sudo apt install ghostscript

	:type input_file: string
	:param input_file: the directory of the PDF before compressoin

	:type output_file: string
	:param output_file: the directory of the PDF after compressoin

	:type resolution: int
	:param resolution: the resolution of the reduced file
	"""
	start_time = time.time()

	try:
		bash_command = '''gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
		-dNOPAUSE -dBATCH -dColorImageResolution={resolution} \
		-sOutputFile={output_file} {input_file}'''
		os.system(bash_command)
	except : 
		logger.error(traceback.format_exc())
	else:
		stop_time = time.time()
		dt = stop_time - start_time
		logger.info("[decrypte completed] {input_file} in {dt}")

def decrypte(input_file, output_file):
	"""
	Decrypte PDF using python library: pikepdf
	Install pikepdf using the folloaing bash comman
		pip install pikepdf

	:type input_file: string
	:param input_file: the directory of the PDF before decryption

	:type output_file: string
	:param output_file: the directory of the PDF after decryption
	"""
	start_time = time.time()
	try:
		import pikepdf					
	except: 
		logger.error(traceback.format_exc())		
	else:
		pdf = pikepdf.open(input_file)
		pdf.save(output_file)
		stop_time = time.time()
		dt = stop_time - start_time
		logger.info(f"[decrypte completed] {input_file} in {dt} s")	

# Test functions
if __name__ == '__main__':
	# decrypte('../tests/in.pdf', '../tests/out.pdf')


