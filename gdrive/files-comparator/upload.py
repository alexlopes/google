import os
import sys
import logging
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload
from apiclient.discovery import build

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

IMAGE_TYPES = ['.jpg']
VIDEO_TYPES = ['.mp4']
folder_id = '0Bx6x3olZsVExNEhvSWNhZzhENjg'


def get_mimetype(filename, filepath):
    d, extension = os.path.splitext(filepath+filename)    
    if extension in IMAGE_TYPES:
        return 'image/jpeg'

def get_drive_service():
    logger.info('Obtaining Drive service')
    # Setup the Drive v3 API
    SCOPES = 'https://www.googleapis.com/auth/drive'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)    

    return build('drive', 'v3', http=creds.authorize(Http()))


def photo_or_video(filename, filepath):    

    file_metadata = {'name': filename, 
                     'parents': [folder_id]
                     }
    mimetype = get_mimetype(filename, filepath)

    media = MediaFileUpload(filepath+'/'+filename,
                            mimetype=mimetype)       

    drive_service = get_drive_service()


    logger.info('Uploading file %s to Google Drive folder %s' % (filepath+filename.encode('utf-8'), folder_id))


    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()

    logger.info('Upload completed for %s File ID: %s' % ( filepath+filename.encode('utf-8'), file.get('id')) )
    
