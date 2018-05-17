from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.discovery import build
import logging

logger = logging.getLogger(__name__)


def get_drive_service(scope):
    logger.info('Obtaining Drive service')
    # Setup the Drive v3 API
    SCOPES = 'https://www.googleapis.com/auth/'+scope
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)    

    return build('drive', 'v3', http=creds.authorize(Http()))