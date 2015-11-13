import requests
import os
import re


SOLR_INDEXR = "http//localhost:8983/solr/" + "%s" + "/update/?commit=true"

GEOTOPIC_PARSER_SERVER = "http://localhost:9997"
CTAKES_SERVER = "http://localhost:9998"
OCR_SERVER = "http://localhost:9999"


def change_extension(file):
    file = re.sub(".*",".geot",file)
    return file

def upload_ner(SERVER, files):
    response = requests.put(SERVER, files = files)
    return response.text


def index_solr(data, server_name):
    server = SOLR_INDEXR % server_name
    response = requests.put(server, data = data)
    return response

if __name__ == '__main__':
    for file in os.listdir(os.getcwd()):

        files = {'upload_file': open(file,'rb')}

        response_ctakes = upload_ner(CTAKES_SERVER, files)
        response_index = index_solr(response_ctakes, "ctakes")

        response_ocr = upload_ner(OCR_SERVER, files)
        response_index = index_solr(response_ocr, "ocr")

        file = change_extension(file)
        response_geo = upload_ner(GEOTOPIC_PARSER_SERVER, files)
        response_index = index_solr(response_geo, "geo")