# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
from upload import photo_or_video

list_drive = []
list_local = []

gdrive_list_filenames_output = "/home/alex/Área de Trabalho/Gramado/file_names_0Bx6x3olZsVExNEhvSWNhZzhENjg.txt"
local_folder_location = "/home/alex/Área de Trabalho/Gramado/Celular_Karina"

if __name__ == '__main__':
    file = open(gdrive_list_filenames_output,"r") 
    for line in file: 
        list_drive.append(line.replace('\n',''))

    local_folder  = local_folder_location
    onlyfiles = [f for f in listdir(local_folder) if isfile(join(local_folder, f))]


    for line in onlyfiles: 
        list_local.append(line)   

    print 'The diff (Local List - Drive List) : >>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< '
    local_to_drive_diff = list(set(list_local) - set(list_drive))
    photo_or_video(local_to_drive_diff[3], local_folder_location)