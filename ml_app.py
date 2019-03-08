#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

import numpy as np
import dcm2Numpy_2 as dcm2np
import getscu
import werkzeug
import subprocess
import os
import sys
sys.path.append("./HepatoPredictCode")

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('Name', dest = 'Name', location = 'form', 
	required = True, help = 'The user\'s username')
#### Print numpy array all element #####
# np.set_printoptions(threshold=np.nan)


##### Test Api : You can test function by the api. #####
class home(Resource):
    def get(self):
        print('\033[0;35;40m\tconnect home page\033[0m ')
        return 'Home Page'
    def post(self):
        print('home post')
        username = request.form.get('Name')
        print(str(username))
        return 'Good call'

class jpg2dcm(Resource):
    def get(self):
        print('\033[0;35;40m\texecute the dcm4chee tool kit\033[0m')
        subprocess.call('/home/jerry/Desktop/HepatoAI/MlServer/dcm4che-5.15.1/bin/jpg2dcm /home/jerry/Desktop/HepatoAI/MlServer/ImgFile/123.jpg \
            /home/jerry/Desktop/HepatoAI/MlServer/DcmFile/3344.dcm', shell = True)
        return 'The jpg file has been convert!!!'

##### After retrieve Dicom file from PACS server, all dicom file read by Numpy. #####
class retrieve(Resource):
    def post(self):
        layer = getscu.check_layer(request.form.get('Study'), request.form.get('Series'), request.form.get('Instance'))
        random_folder = getscu.folder_manage()
        getscu_status = getscu.connect_pacs(request.form, request.form.get('Study'), request.form.get('Series'), 
            request.form.get('Instance'), layer, random_folder)
        #print('\033[0;35;40m\tRetrieve Diocm file from PACS server\033[0m')
        #print(dcm2np.np_combine(random_folder))
        input = dcm2np.np_combine(random_folder)

        # Inference
        from inference_api import LiverInference
        LiverInferenceClass = LiverInference()
        print(LiverInferenceClass.inference(input,spacing=4.0))
        return 'finished', 200
        
api.add_resource(home, '/home/')
api.add_resource(jpg2dcm, '/dwv-ml/')
api.add_resource(retrieve, '/dwv-ml/retrieve/')

if __name__ == '__main__':
    app.run(debug=True, host='10.34.45.43', port=3303)
