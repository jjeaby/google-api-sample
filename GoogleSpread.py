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

    def create(self):
        # gc.del_spreadsheet("1xCD3c6F9AvQH9uT86wy678W80KoUwvOw")
        gs = self.gc.create("test.xls", folder_id='1xCD3c6F9AvQH9uT86wy678W80KoUwvOw')
        # worksheet = gs.add_worksheet(title='Sheet1', rows='1', cols='1')
        worksheet = gs.worksheet(title='Sheet1')
        worksheet.update_acell('A1', 'a1')
        worksheet.update_acell('B1', 'b1')
        worksheet.update_acell('A2', 'a2')
        worksheet.update_acell('B2', 'b2')
        gs.share('jjeaby.ec1@gmail.com', perm_type='user', role='writer')

    def read(self):
        gc1 = self.gc.open("test.xls").worksheet('시트1')
        # gc1.update_acell('B2', 'novels')
        gc2 = gc1.get_all_values()
        print(gc2)

        # sh = gc.open("python-linkage-sample")


if __name__ == '__main__':
    GoogleSpread().create()
