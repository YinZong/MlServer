#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pydicom
import os
import PIL # optional
import subprocess, sys
from PIL import Image
import numpy as np

def np_combine(foldername):
    result_array = None
    for file_name in sorted(os.listdir('./retrieve/' + foldername)) :
        file_path = os.path.join('./retrieve/' + foldername, file_name)
        ds = pydicom.dcmread(file_path)
        temp_array = np.expand_dims(ds.pixel_array, axis=0)
        print('\033[0;35;40m\t' + file_name + '\033[0m')
        if result_array is None :
            result_array = temp_array
        else :
            result_array = np.concatenate((result_array,temp_array),axis=0)
    return np.rollaxis(result_array, 0, 3)