#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pydicom
import os
import PIL # optional
import json
import subprocess, sys
from PIL import Image
import numpy as np

# response_template = {'prediction_array' : 'Prediction Results'}


def file_arrange(foldername):
    num_files = 0
    for fileName in os.listdir('./static/retrieve/' + foldername + '/'):
        num_files = num_files + 1

    arrange_array = []

    for file_name in sorted(os.listdir('./static/retrieve/' + foldername)) :
        file_path = os.path.join('./static/retrieve/' + foldername, file_name)
        ds = pydicom.dcmread(file_path)
        arrange_array.insert(int(ds.InstanceNumber) - 1, file_name)
    return arrange_array


def np_combine(foldername, sequence):
    result_array = None
    print(type(result_array))
    for filename in sequence:
        file_path = os.path.join('./static/retrieve/' + foldername, filename)
        ds = pydicom.dcmread(file_path)
        print('\033[0;35;40m\t' + str(ds.InstanceNumber) + '\033[0m')
        temp_array = np.expand_dims(ds.pixel_array, axis=0)
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
