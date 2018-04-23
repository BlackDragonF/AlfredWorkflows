#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import requests
import uuid
import shutil

# extract template_name and sentences from inputs
inputs = '{query}'.split(None, 1)
template_name = inputs[0]
sentences = inputs[1].split('|')

# generate api
api = 'https://sorry.xuty.tk/api/' + template_name +'/make'

# create, fill and jsonify post body
parameters = {}
index = 0
for sentence in sentences:
    # format: {"0", "...", "1", ...}
    parameters[str(index)] = sentence
    index = index + 1
parameters = json.dumps(parameters)

# use requests to post request to server
reponse = requests.post(api, data = parameters, timeout = 3)

# retrieve return code and generate output
return_code = reponse.status_code
output = 'failed' # error: output set to 'failed'
if return_code == 200:
    # branch: request succeeded, download image to tmp directory
    download = 'https://sorry.xuty.tk' + reponse.text
    response = requests.get(download, stream = True, timeout = 10)

    # create temp directory(if not exists) to save gifs
    temp_directory = os.environ['HOME'] + '/Downloads/'
    if not os.path.exists(temp_directory):
        os.mkdir(temp_directory)

    # download image
    image_path = temp_directory + str(uuid.uuid1()) + '.gif' # use uuid to generate an unique filename
    with open(image_path, 'wb') as image:
        shutil.copyfileobj(response.raw, image)

    # copy downloaded meme to clipboard
    return_value = os.system('./gif2clipboard %s' % image_path)
    if return_value == 0:
        # branch: copy succeeded, output set to 'succeeded'
        output = 'succeeded'

sys.stdout.write(output)