from django.shortcuts import render
from django.http import HttpResponse
from mapper.models import Record
from django.core import serializers

import json

# Create your views here.
def index(request):
    # results = readFile("json", "mapper/test_data/test1.json")
    results = readFile("csv", "mapper/test_data/test2.csv")

    persons = []
    for p in results:
        person = Record(**p)
        persons.append(serializers.serialize('json', [ person, ]))

    return HttpResponse(persons)

def readFile(fileType, fileName):
    if (fileType == "json"):
        return parseJsonFile(fileName)
    if (fileType == "csv"):
        return parseCSVFile(fileName)
        
def parseJsonFile(fileName):
    f = open(fileName, "r")
    result = []
    metadata = getMetadata()
    for x in f:
        result.append(jsonTranslator(metadata, x))
    return result

def parseCSVFile(fileName):
    f = open(fileName, "r")
    result = []
    metadata = getMetadata()
    for x in f:
        result.append(csvTranslator(metadata, x))
    return result

def getMetadata():
    metadata = {
        "fileType": "json",
        "delimiter": ",",
        "fields": {
            "name1": {
                "destination": "first_name",
                "column": 0
            },
            "name2": {
                "destination": "last_name",
                "column": 1
            }
        }
    }
    return metadata

def jsonTranslator(metadata, source):
    result = {}
    json_source = json.loads(source)
    for key in metadata['fields']:
        destination_key = metadata['fields'][key]['destination']
        val = json_source[key]
        result[destination_key] = val

    return result


def csvTranslator(metadata, source):
    result = {}
    columns = source.split(metadata['delimiter'])
    for key in metadata['fields']:
        destination_key = metadata['fields'][key]['destination']
        val = columns[metadata['fields'][key]['column']]
        result[destination_key] = val

    return result
