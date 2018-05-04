from os import listdir
from os.path import isfile, join


list_drive = []
list_local = []

if __name__ == '__main__':
    file = open("OUTPUTFILENAME_HERE.txt","r") 
    for line in file: 
        list_drive.append(line.replace('\n',''))

    local_folder  = 'LOCAL_FOLDER_NAME_HERE'
    onlyfiles = [f for f in listdir(local_folder) if isfile(join(local_folder, f))]


    for line in onlyfiles: 
        list_local.append(line)   

    print 'The diff (Local List - Drive List) : >>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< '
    print(list(set(list_local) - set(list_drive)))