import os
import shutil

def find_and_transfer(adoc_folder, project_folder):
    """
    Переносит файлы с переводом и суффиксом '_code-alpha2' в папки, где находятся их аналогичные файлы без перевода. Example,'_code-alpha2': _ru, _sr, _es.
    """
    # Список файлов с переводом
    translated_files = [f for f in os.listdir(adoc_folder) if f.endswith("_code-alpha2".adoc")]

    for translated_file in translated_files:
        # Получаем оригинальное имя файла (без '_code-alpha2')
        original_file_name = translated_file.replace("_code-alpha2", "")

        file_moved = False  # Флаг для успешного копирования

        # Идём по директориям в проекте
        for root, dirs, files in os.walk(project_folder):
            if original_file_name in files:
                # Перемещаем файл на место найденного эквивалента
                source_path = os.path.join(adoc_folder, translated_file)
                destination_path = os.path.join(root, translated_file)

                shutil.move(source_path, destination_path)
                print(f"Файл '{translated_file}' перемещен в '{root}'")
                file_moved = True
                break

        if not file_moved:
            print(f"Двойник для файла '{translated_file}' не найден в проекте.")

# Пример путей к исследованиям
adoc_folder = "/Users/.../adoc_files"
project_folder = "/Users/.../lessons/"

# Запуск поиска и переноса
find_and_transfer(adoc_folder, project_folder)
