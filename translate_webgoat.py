#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:01:53 2024

@author: BoyarD1
"""

import os
import requests
from requests.exceptions import RequestException
from tenacity import retry, wait_fixed, stop_after_attempt


# --- Настройки Yandex Translate ---
IAM_TOKEN_PATH = '/Users/.../'Your token in.txt'  # Путь к файлу с IAM-токеном в txt файле
folder_id = 'inject your folder'  # Идентификатор каталога в Yandex.Cloud
target_language = 'code country Alpha2'
source_language = 'en'
# -------------------------------------

def read_iam_token(token_path):
    """Читает IAM токен из файла."""
    try:
        with open(token_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Файл IAM-токена не найден.")
        return None

@retry(wait=wait_fixed(2), stop=stop_after_attempt(5))

def translate_text_yandex(text):
    """Переводит текст с помощью Yandex Translate API."""
    IAM_TOKEN = read_iam_token(IAM_TOKEN_PATH)
    if not IAM_TOKEN:
        return None

    body = {
        "sourceLanguageCode": source_language,
        "targetLanguageCode": target_language,
        "texts": [text],
        "folderId": folder_id,
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {IAM_TOKEN}"
    }
    
    try:
        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                json=body, headers=headers)
        response.raise_for_status()
        return response.json().get('translations', [{}])[0].get('text')
    except RequestException as e:
        print(f"Ошибка сетевого запроса: {e}")
        return None

# --- Основная часть скрипта ---
folder_path = '/Users/.../adoc_files/'  # Путь к папке с .adoc файлами. В adoc_files собраны все найденные в проекте файлы лекций

for filename in os.listdir(folder_path):
    if filename.endswith(".adoc"):
        base_filepath = os.path.join(folder_path, filename)

        with open(base_filepath, "r", encoding="utf-8") as f:
            english_text = f.read()

        # Переводим текст
        translated_text = translate_text_yandex(english_text)

        # Создаем файл перевода только если перевод успешен
        if translated_text:
            translated_filename = filename.replace(".adoc", f"_{target_language}.adoc")
            translated_filepath = os.path.join(folder_path, translated_filename)

            with open(translated_filepath, "w", encoding="utf-8") as f:
                # Записываем сначала перевод, затем исходный текст
                f.write(translated_text)
                f.write("\n\nИсходный текст (EN):\n")
                f.write(english_text)
                
               

            print(f"Файл '{filename}' успешно переведен и сохранен как '{translated_filename}'")
