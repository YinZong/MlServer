#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import json
import subprocess

with open('./config.json', 'r') as reader:
    config_dict = json.loads(reader.read());

typeLayer = ['PATIENT', 'STUDY', 'SERIES', 'IMAGE', 'FRAME']
GETSCU_CMD = config_dict['dcmtool_path'] + 'getscu -L '

FOLDER_BUFFER = config_dict["folder_buffer"]

def check_layer(study, series, instance):
    if(study != '' and series != '' and instance != ''):
        return 3
    if(study != '' and series != ''):
        return 2
    if(study != ''):
        return 1

def connect_pacs(formdata, studyID, seriesUID, instanceUID, layer, foldername):
    connect = formdata.get('Title') + "@" + formdata.get('ipAddr') + ":" + formdata.get('Port')
    print(connect)
    if(layer == 1):
        subprocess.call(GETSCU_CMD + typeLayer[layer] + " -c " + connect + " -m 0020000D=" + studyID + 
            " --directory ./static/retrieve/" + foldername + "/", shell = True)
    if(layer == 2):
        subprocess.call(GETSCU_CMD + typeLayer[layer] + " -c " + connect + " -m 0020000D=" + studyID + 
            " -m 0020000E=" + seriesUID + " --directory ./static/retrieve/" + foldername + "/", shell = True)
    if(layer == 3):
        subprocess.call(GETSCU_CMD + typeLayer[layer] + " -c " + connect + " -m 0020000D=" + studyID + 
            " -m 0020000E=" + seriesUID + " -m 00080018=" + instanceUID + " --directory ./static/retrieve/" + foldername + "/", shell = True)

def folder_empty(older):
    for fileName in os.listdir('./static/retrieve/' + older + '/'):
        os.remove('./static/retrieve/' + older + '/' + fileName)

def buffer_check(path):
    num_folders = 0
    older = 0
    name_list = []
    ##計算路徑內有幾個資料夾
    for fileName in os.listdir(path):
        name_list.append(fileName)
        num_folders = num_folders + 1
    print(num_folders)
    print(name_list)
    if(num_folders >= FOLDER_BUFFER):
        t = time.strftime("%Y%m%d%H%M%S")
        for i in range(len(name_list)):
            diff_time = int(t) - int(name_list[i])
            if(diff_time > older):
                older = diff_time
                older_name = name_list[i]
        folder_empty(older_name)
        os.rmdir('./static/retrieve/' + older_name)

def folder_manage():
    folder_name = time.strftime("%Y%m%d%H%M%S")
    print('\033[0;35;40m\t' + folder_name + '\033[0m')
    buffer_check('./static/retrieve/')
    os.mkdir('./static/retrieve/' + folder_name)
    return folder_name