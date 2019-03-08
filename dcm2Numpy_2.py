#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pydicom
import os
import PIL # optional
import json
import subprocess, sys
from PIL import Image
import numpy as np

response_template = {'prediction_array' : 'Prediction Results'}

def sort_files(foldername):
    for file_name in sorted(os.listdir('./static/retrieve/' + foldername)) :

def np_combine(foldername):
    result_array = None
    print(type(result_array))
    for file_name in sorted(os.listdir('./static/retrieve/' + foldername)) :
        file_path = os.path.join('./static/retrieve/' + foldername, file_name)
        ds = pydicom.dcmread(file_path)
        temp_array = np.expand_dims(ds.pixel_array, axis=0)
        print('\033[0;35;40m\t' + file_name + '\033[0m')
        if result_array is None :
            result_array = temp_array
        else :
            result_array = np.concatenate((result_array,temp_array),axis=0)
    print(type(result_array))
    return result_array
    #return np.rollaxis(result_array, 0, 3)
    # response_template['prediction_array'] = str(result_array)
    # return json.dumps(response_template)

print(os.path.dirname(__file__))
