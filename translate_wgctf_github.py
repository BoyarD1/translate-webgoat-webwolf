#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 00:15:07 2024

@author: BoyarD1
"""

import os
import requests
from shutil import copyfile

# --- Yandex Translate Settings ---
IAM_TOKEN_PATH = '/.../../IAM_token.txt' # Path to the IAM token file
folder_id = 'Your folder_id' # Folder ID in Yandex.Cloud
target_language = '*' # Add target language
source_language = '*' # Add source language 
# -------------------------------------

# --- Function for text translation using Yandex Translate API ---
def translate_text_yandex(text):
    # "Translates text using the Yandex Translate API."

    with open(IAM_TOKEN_PATH) as f:
        IAM_TOKEN = f.read().strip()
    
    body = {
        "sourceLanguageCode": source_language,
        "targetLanguageCode": target_language, 
        "texts": [text], 
        "folderId": folder_id,
        }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body, headers=headers)

    if response.status_code == 200:
        return response.json()['translations'][0]['text'] 
    else:
        print(f"Translation Error: {response.status_code}")
        print(response.text)
        return None
# ---------------------------------------------------------------------

# --- Main part of the script ---
folder_path = '/.../adoc_files' # Path to the folder with .adoc files

for filename in os.listdir(folder_path):
    if filename.endswith(".adoc"):
        new_filename = filename.replace(".adoc", f"_{target_language}.adoc")
        if not os.path.exists(os.path.join(folder_path, new_filename)):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                english_text = f.read()
            
            # Translate the text with Yandex Translate
            russian_text = translate_text_yandex(english_text) 

            if russian_text: # Check that the translation is received
                copyfile(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

                with open(os.path.join(folder_path, new_filename), "w", encoding="utf-8") as f:
                    f.write(russian_text)

                print(f"File '{filename}' successfully translated and saved as '{new_filename}'")
