#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Wenbin Fei, Email: wenbinfei@gmail.com
# All rights reserved.

"""
Batch deal with your files.
"""
import os
import logging.config
import time

# Create logger
logging.config.fileConfig(fname='logging.ini')
logger = logging.getLogger(__name__)

def copy_filter(input_dir, output_dir, include_file_type):
    """
    Copy files with certain extensions using bash command: rsync
    Default setting is to copy
    todo: add exclude type

    :type input_dir: string
    :param input_dir: the directory of the folder that original files in, end with /
    e.g. /root/mnt/WF/Joost_shared/ /root/mnt/To-laptop/Joost_shared/

    :type output_dir: string
    :param output_dir: the directory of the folder that target files to be moved in

    :type include_file_type: tuple
    :param include_file_type: a tuple of the extenstion of files to be moved
    """
    start_time = time.time()
    try:
        include_command = ""
        for i in include_file_type:           
            include_command = include_command + " --include '*."+ i + "'"
        bash_command = "rsync -a --include '*/'" + include_command + " --exclude '*' " + \
                        input_dir + ' ' + output_dir
        print(bash_command)
        os.system(bash_command)
    except: 
        logger.error('[copy_filter failed]')
        logger.error(traceback.format_exc())
    else:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"[copy_filter completed] {input_dir} in {dt} s")


if __name__ == '__main__':
    # test copy_filter on ubuntu. I used WSL on my windows computer
    copy_filter(r"/mnt/c/Wenbin/GitHub/revamp/tests/individual/", r"/mnt/c/Wenbin/GitHub/revamp/tests/individual-copy_filter/", ['txt', 'JPG'])