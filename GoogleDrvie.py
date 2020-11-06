from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class GoogleDrive():
    def __init__(self):
        """
        인증 정보를 설정하는 부분
        """
        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
                  'https://www.googleapis.com/auth/drive.file']

        creds = service_account.Credentials.from_service_account_file("./credential/google_api_service_account.json",
                                                                      scopes=SCOPES)
        # return Google Drive API service
        self.gdrive = build('drive', 'v3', credentials=creds)


    def get_file_list(self):
        """
        Google Drive 의 폴더/파일을 file_id, name, mimeType 등의 정보로 가져오는 코드
        pagesize 를 100으로  설정 
        """
        service = self.gdrive
        # Call the Drive v3 API
        results = service.files().list(
            pageSize=100, fields="nextPageToken, files(id, name, mimeType, size, parents, modifiedTime)").execute()
        # get the results
        items = results.get('files', [])
        # list all 20 files & folders
        files = self.list_files(items)
        #for file in files:
        #    print(file)
        return files


    def get_size_format(self, b, factor=1024, suffix="B"):
        """
        Scale bytes to its proper byte format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
            if b < factor:
                return f"{b:.2f}{unit}{suffix}"
            b /= factor
        return f"{b:.2f}Y{suffix}"


    def list_files(self, items):
        """given items returned by Google Drive API, prints them in a tabular way"""
        if not items:
            # empty drive
            print('No files found.')
        else:
            rows = []
            for item in items:
                # get the File ID
                id = item["id"]
                # get the name of file
                name = item["name"]
                try:
                    # parent directory ID
                    parents = item["parents"]
                except:
                    # has no parrents
                    parents = "N/A"
                try:
                    # get the size in nice bytes format (KB, MB, etc.)
                    size = self.get_size_format(int(item["size"]))
                except:
                    # not a file, may be a folder
                    size = "N/A"
                # get the Google Drive type of file
                mime_type = item["mimeType"]
                # get last modified date time
                modified_time = item["modifiedTime"]
                # append everything to the list
                rows.append({
                    "id": id, "name": name,
                    "parents": parents,
                    "size": size,
                    "mime_type": mime_type,
                    "modified_time": modified_time
                })
            return rows


    def upload_files(self, folder_id='', file=''):
        """
        Creates a folder and upload a file to it
        """
        service = get_gdrive_service()
        print("Folder ID:", folder_id)
        # upload a file text file
        # first, define file metadata, such as the name and the parent folder ID
        file_metadata = {
            "name": file,
            "parents": [folder_id]
        }
        # upload
        media = MediaFileUpload(file, resumable=True)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print("File created, id:", file.get("id"))


    def delete_files(self, file_id=''):
        """
        Creates a folder and upload a file to it
        """
        service = get_gdrive_service()
        service.files().delete(fileId=file_id).execute()
        print("File delete, id:", file_id)


if __name__ == '__main__':
    gdrive = GoogleDrive() 
    # upload_files(folder_id='1sChbkWKnHs9nQlZhkqFKJh0XGuZyFj71', file="requirements.txt")
    # delete_files(file_id='1D8A0pJHyRhDJX6bTXom6S0TPDs4KMxlw')
    files = gdrive.get_file_list()
    for file in files:
        print(file)
