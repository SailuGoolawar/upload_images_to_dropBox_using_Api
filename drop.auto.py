# ----------------------------------------------------------------------------------------------------------------------
# Script        : drop.auto.py
# Author        : Sailu Goolawar
# Created On    : 25/02/2021
# Dependencies  : requests, io, csv, json, Image from PIL , os
# Description   : this script will useful to upload images to dropBox folder using API
# Last Modified : 25/02/2021
# ----------------------------------------------------------------------------------------------------------------------
import requests
import json
import io
from PIL import Image
import os

# api end point to upload files
endpoint = "https://content.dropboxapi.com/2/files/upload"
# token
token = "< access token >"
# local folder path 
local_files_link = "< local images folder path >"
# destination path of dropbox
dropbox_folder = "< dropBox destination path >"


# http post request function
def http_post (strApi, strData, strHeader):
    strResponse = requests.post(strApi, strData, headers=strHeader)
    return (strResponse)

# getting all the files from the given folder
files_list = os.listdir(local_files_link)

# iterating all the files in the folder
for file in files_list:
    # header for post request to api endpoint
    headers = {
        "Content-Type": "application/octet-stream",
        "Authorization": "Bearer "+token
    }
    # forming the image actual path
    image_file_path = local_files_link+"/"+file
    # opening the image using Image.open()
    fileData = Image.open(image_file_path, 'r')
    # BytesIO to format the image to binary
    bytesarr = io.BytesIO()
    # formatting the image into binary with the file format
    fileData.save(bytesarr, format=fileData.format)
    # getting the actual binary of the image
    bytesarr = bytesarr.getvalue()
    # include 'Dropbox-API-Arg' in headers with path as dropbox destination folder with image
    headers['Dropbox-API-Arg'] = json.dumps({'path': dropbox_folder+file})
    # api call
    response = http_post(endpoint, bytesarr, headers)
    # response
    print(response)
    # response text
    print(response.text)

