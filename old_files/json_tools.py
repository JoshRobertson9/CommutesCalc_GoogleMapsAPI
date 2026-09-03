# Existing Modules
import json
import requests
import csv

"""
def get_data_from_cache(file_name):
    try:
        with open('file_name', 'r') as file:
            cache = json.load(file)
        return cache
    except FileNotFoundError:
        return {}
"""

# Updates empty or existing json file
def update_cache(file_name, new_data):
    try:
        with open(file_name, 'r') as file:
            try:
                cache = json.load(file)
            except json.decoder.JSONDecodeError:
                # If file is empty or not valid JSON, initialize an empty cache
                cache = {}
    except FileNotFoundError:
        cache = {}

    cache.update(new_data)

    with open(file_name, 'w') as file:
        json.dump(cache, file, indent = 4)
