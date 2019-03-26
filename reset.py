#!/usr/bin/python
# -*- coding: UTF-8 -*-
import shutil
import os

folder_path = ["./static/DcmFile/", "./static/ImgFile/", "./static/retrieve/"]

for i in folder_path:
	print(i)
	shutil.rmtree(i)
	os.makedirs(i)
	print('Create folder : ' + i)
