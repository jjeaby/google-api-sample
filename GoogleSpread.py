import gspread
from google.oauth2.service_account import Credentials


class GoogleSpread:

    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
                  'https://www.googleapis.com/auth/drive.file']

        CREDENTIALS = Credentials.from_service_account_file(
            './credential/google_api_service_account.json',
            scopes=SCOPES
        )
        self.gc = gspread.authorize(CREDENTIALS)

    def create(self,filename):
        gs = self.gc.create(filename, folder_id='1xCD3c6F9AvQH9uT86wy678W80KoUwvOw')
        worksheet = gs.worksheet(title='Sheet1')
        worksheet.update_acell('A1', 'a1')
        worksheet.update_acell('B1', 'b1')
        worksheet.update_acell('A2', 'a2')
        worksheet.update_acell('B2', 'b2')
        gs.share('jjeaby.ec1@gmail.com', perm_type='user', role='writer')

    def update(self, filename):
        gc1 = self.gc.open(filename).worksheet('Sheet1')
        gc1.update_acell('B2', 'novels')
        
    def read(self, filename):
        gc1 = self.gc.open(filename).worksheet('Sheet1')
        gc2 = gc1.get_all_values()
        return gc2 

if __name__ == '__main__':
    gs = GoogleSpread()
    gs.create('test_sheet')
    sheet_text = gs.read('test_sheet')
    print(sheet_text)
    gs.update('test_sheet')
    sheet_text = gs.read('test_sheet')
    print(sheet_text)
    

