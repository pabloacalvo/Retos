import os
import humanize

main_root = os.path.dirname(os.path.abspath(__file__))
input_path = input("Nombre de la carpeta a analizar: ")

analyze_folder = os.path.join(main_root, input_path)
list_files = os.listdir(analyze_folder)


total_size = sum(os.stat(os.path.join(analyze_folder,file)).st_size for file in list_files if os.path.isfile(os.path.join(analyze_folder,file)))
print('---Analysis report---')
print(f"Total files: {len(list_files)}")
print(f"Tamaño total de la carpeta: {humanize.naturalsize(total_size,binary=True)}")

for index,file in enumerate(list_files,1):
    completed_root = os.path.join(analyze_folder,file)
    if os.path.isfile(completed_root):
        stadistics = os.stat(completed_root)
        print(f'{index}- Archivo: {file} - Tamaño: {humanize.naturalsize(stadistics.st_size, binary=True)}')
