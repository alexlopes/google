# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
from upload import photo_or_video
from auth import get_drive_service
from listing import list_files_by_folder_id


drive_list_files = []
list_local = []

local_folder_location = "/home/alex/Pictures/"

folder_id = '??'

if __name__ == '__main__':
    drive_service = get_drive_service('drive.metadata.readonly')
    
    drive_list_files = list_files_by_folder_id(folder_id, drive_service) 
    

    # file = open(gdrive_list_filenames_output,"r") 
    # for line in file: 
    #     list_drive.append(line.replace('\n',''))

    local_folder  = local_folder_location
    onlyfiles = [f for f in listdir(local_folder) if isfile(join(local_folder, f))]


    for line in onlyfiles: 
        list_local.append(line)   

    print 'The diff (Local List - Drive List) : >>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< '
    #local_to_drive_diff = list(set(list_local) - set(drive_list_files))
    #print local_to_drive_diff
    drive_service = get_drive_service('drive')
    for f in list_local:
        if f in drive_list_files:            
            print 'Ja existe no drive', f
        else:
            print 'Nao existe no drive', f
            photo_or_video(f, local_folder_location, drive_service, folder_id)