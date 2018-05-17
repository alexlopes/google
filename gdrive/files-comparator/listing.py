
def list_files_by_folder_id(folder_id, drive_service):
    drive_files = []
    page_token = None
    while True:
        response = drive_service.files().list(q="parents='%s'" % folder_id,
                                              spaces='drive',
                                              fields="nextPageToken, files(id, name, parents)",
                                              pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            #print 'Found file: %s (%s) - (%s)' % (file.get('name'), file.get('id'), file.get('parents'))
            drive_files.append(file.get('name'))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break    
    return drive_files