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
import traceback
import shutil
import re

# Create logger
logging.config.fileConfig(fname='logging.ini')
logger = logging.getLogger(__name__)

def folder_tree(input_dir, folder_names):
    """
    Create subfolders based on a give list of folder names.   

    :type input_dir: string
    :param input_dir: the directory of the folder that subfolders or files in    

    :type folder_names: list
    :param folder_names: a list of strings to store the names of desired subfolders.
    """
    start_time = time.time()
    try:
        path_list = [line.strip() for line in open(input_dir,'r')]
        for path in path_list:
            for name in folder_names:
                path_subfolder = path + '/' + name
                if not os.path.exists(path_subfolder):
                    os.makedirs(path_subfolder) 
    except: 
        logger.error('[folder_tree failed]')
        logger.error(traceback.format_exc())
    else:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("[folder_tree completed] {} in {:.4f} s".format(input_dir, dt))

def dir_list(input_dir, output_path, only_folder=True, certain_file=False):
    """
    Create a dir_list.txt (you shold name this in the output_path) for the subfolders and/or files in a folder.    

    :type input_dir: string
    :param input_dir: the directory of the folder that subfolders or files in    

    :type output_dir: string
    :param output_dir: the directory of a file which contains the directorids. e.g. XXX/XXX.dir_list.txt

    :type only_folder: boolean
    :param only_folder: True-only export the subfolder directory.

    :type only_folder: str
    :param only_folder: default is False to include all files/folder. Specify a file name or extains as a filter.
    """
    start_time = time.time()
    try:
        sub_dirs = os.listdir(input_dir)
        print(sub_dirs)
        if only_folder == True:
            for term in sub_dirs:
                print (term)
                if ("." in term):  #files usually has an estension name with a symbol '.'
                    sub_dirs.remove(term)
        print(sub_dirs)
        counter = 0
        with open(output_path,'w') as f:
            while counter != (len(sub_dirs)) - 1: 
                sub_dir = sub_dirs[counter]         
                if certain_file:
                    if certain_file in sub_dir:
                        f.write(input_dir + '/' + sub_dir + '\n')                
                else:                
                    f.write(input_dir + '/' + sub_dir + '\n')
                counter += 1

            sub_dir = sub_dirs[-1]  # only for the last line without '\n'        
            if certain_file:
                if certain_file in sub_dir:
                    f.write(input_dir + '/' + sub_dir)                
            else:                
                f.write(input_dir + '/' + sub_dir)
            
    except: 
        logger.error('[dir_list failed]')
        logger.error(traceback.format_exc())
    else:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("[dir_list completed] {} in {:.4f} s".format(input_dir, dt))


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
        logger.info("[copy_filter completed] {} in {:.4f} s".format(input_dir, dt))

def batch_rename_folder(input_dir, re_match, str_new):    
    """
    Change the folder name using regular expression.
    it do same as using e.g. re.sub('-v([0-9]*)' ,'-v800', path)      

    :type input_dir: string
    :param input_dir: a dir.txt file save the directory of the folders to be named
    
    :type re_match: string
    :param re_match: regular express to locate the string to be changed.
    
    :type str_new: string
    :param str_new: new string to change the string in the old folders name
    """
    start_time = time.time()
    try:
        path_list = [line.strip() for line in open(input_dir,'r')]
        for path in path_list:
            new_name = re.sub(re_match ,str_new, path)    
            os.rename(path.encode('unicode_escape'), new_name.encode('unicode_escape'))
            logger.info("[rename_folder completed] {} ".format(path))
    except: 
        logger.error('[batch_rename_folder failed]')
        logger.error(traceback.format_exc())
    else:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("[batch_rename_folder completed] {} in {:.4f} s".format(input_dir, dt))

def batch_rename_file(input_dir, file_extension, re_match, str_new):    
    """
    Change the the name of files with certain extension
    it do same as using e.g. re.sub('-v([0-9]*)' ,'-v800', path)      

    :type input_dir: string
    :param input_dir: a dir_list.txt file save the directory of the folders containing the certain files

    :type file_extension: list
    :param file_extension: a list of certain extension of file

    :type re_match: string
    :param re_match: regular express to locate the string to be changed.
    
    :type str_new: string
    :param str_new: new string to change the string in the old folders name
    """
    start_time = time.time()
    try:
        path_list = [line.strip() for line in open(input_dir,'r')]
        for path in path_list:
            for filename in os.listdir(path):
                for i in file_extension:
                    if filename.endswith(i):
                        new_name = re.sub(re_match,str_new,filename)
                        old_file_path = path + '/' + filename
                        new_file_path = path + '/' + new_name
                        os.rename(old_file_path, new_file_path)
                        logger.info("[rename_file completed] {} ".format(old_file_path))
    except: 
        logger.error('[batch_rename_file failed]')
        logger.error(traceback.format_exc())
    else:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("[batch_rename_file completed] {} in {:.4f} s".format(input_dir, dt))

def batch_delete_folder(input_dir, sub_folder = False):    
    """
    Batch delete folders. Or specify a sub_folder to be deleted

    :type input_dir: string
    :param input_dir: a dir_list.txt file save the directory of the folders to be named

    :type sub_folder: list
    :param sub_folder: default is False not for subfolder.
     Giving a list of subfolders to only delete the subfolders
    """
    start_time = time.time()
    try:
        path_list = [line.strip() for line in open(input_dir,'r')]        
        for path in path_list:       
            if isinstance(sub_folder, list):
                for name in sub_folder:
                    path_remove = path + '/' + name
                    shutil.rmtree(path_remove)
            else:
                shutil.rmtree(path)
    except: 
        logger.error('[batch_delete_folder failed]')
        logger.error(traceback.format_exc())
    else:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("[batch_delete_folder completed] {} in {:.4f} s".format(input_dir, dt))

if __name__ == '__main__':
    # test copy_filter on ubuntu. I used WSL on my windows computer
    # copy_filter(r"/mnt/c/Wenbin/GitHub/revamp/tests/individual/", r"/mnt/c/Wenbin/GitHub/revamp/tests/individual-copy_filter/", ['txt', 'JPG'])
    # batch_rename_folder(r"C:\Wenbin\GitHub\revamp\tests\dir_list.txt", '-v([0-9]*)', '-v800')
    # batch_rename_file(r"C:\Wenbin\GitHub\revamp\tests\dir_list.txt", ['txt'], '-v([0-9]*)', '-v200')
    dir_list(r'C:\Wenbin\GitHub\revamp\tests', r'C:\Wenbin\GitHub\revamp\tests\dir_list.txt', True)
    # folder_tree(r"C:\Wenbin\GitHub\revamp\tests\dir_list.txt", ['a', 'b', 'c'])
    # batch_delete_folder(r"C:\Wenbin\GitHub\revamp\tests\dir_list.txt")