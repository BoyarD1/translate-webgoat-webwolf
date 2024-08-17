#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 00:25:44 2024

@author: BoyarD1

"""

import os
import shutil

def transfer_translations(adoc_folder, project_folder):
  """
  Transfers lesson translation files to the appropriate project folders.

  Args:
      adoc_folder: The path to the folder with the .adoc files.
      project_folder: The path to the root folder of the webgoatCTF project.
  """
  for filename in os.listdir(adoc_folder):
    if filename.endswith("_ru.adoc"): # Searching for translated files
      # Forming the filename with the English text
      original_filename = filename.replace("_ru.adoc", ".adoc")

      # Searching for the file with the English text in the project folder
      for root, _, files in os.walk(project_folder):
        if original_filename in files:
          source_path = os.path.join(adoc_folder, filename)
          destination_path = os.path.join(root, filename)

          # Moving the translated file
          shutil.move(source_path, destination_path)
          print(f"File '{filename}' moved to '{root}'")
          break

# Specifying paths to folders
adoc_folder = "/.../adoc_files/" 
project_folder = "/.../" # Replace with actual project path

# Running the file transfer function
transfer_translations(adoc_folder, project_folder)
