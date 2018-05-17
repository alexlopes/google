import os
import sys
import logging
from apiclient.http import MediaFileUpload

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

IMAGE_TYPES = ['.jpg']
VIDEO_TYPES = ['.mp4']


def get_mimetype(filename):
    d, extension = os.path.splitext(filename)    
    if extension in IMAGE_TYPES:
        return 'image/jpeg'


def photo_or_video(filename, filepath, drive_service, folder_id):    

    logger.info('Prepare to upload file %s to Google Drive folder %s' % (filepath+filename.encode('utf-8'), folder_id))
    
    file_metadata = {'name': filename, 
                     'parents': [folder_id]
                     }
    mimetype = get_mimetype(filename)

    media = MediaFileUpload(filepath+'/'+filename,
                            mimetype=mimetype)       

    logger.info('Uploading file %s to Google Drive folder %s' % (filepath+filename.encode('utf-8'), folder_id))


    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()

    logger.info('Upload completed for %s File ID: %s' % ( filepath+filename.encode('utf-8'), file.get('id')) )
    
