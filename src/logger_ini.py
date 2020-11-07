#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Wenbin Fei, Email: wenbinfei@gmail.com
# All rights reserved.

"""
Create a logger
===============
To create a logger in other files, usingt the following code
	import logger_ini
	logger = logger_ini.logger_run()
"""
import logging.config

def logger_run():
	"""
	Create a logger to be used in other files.
	The reason to create a logger in a sepearted file is becasue
	Sphinx may change the current working directory to one of its subdirectories and
	result in that the relative path is not correct.

	Using absolute path when using Sphinx.
	To provide for other users, change it to "logging.ini"

	"""
	logging.config.fileConfig(fname="C:/Wenbin/GitHub/revamp/src/logging.ini") # To provide for other users, change it to "logging.ini"
	logger = logging.getLogger(__name__)
	return logger

