from google.oauth2 import service_account
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.file']
store = file.Storage('storage.json')
creds = store.get()


if not creds or creds.invalid:
    print("make new storage data file ")
    creds = service_account.Credentials.from_service_account_file("./resource/ailinggo-unown-service_account.json",
                                                                  scopes=SCOPES)

DRIVE = build('drive', 'v3', credentials=creds)

FILES = (
    ('requirements.txt'),
)

folder_id = '1aPvE-UPCw-3tGpH78ElwL5msRLUWDrKW'

for file_title in FILES :
    file_name = file_title
    metadata = {'name': 'requirements.txt',
                'parents' : [folder_id],
                'mimeType': None
                }

    res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
    if res:
        print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))