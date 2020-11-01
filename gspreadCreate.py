import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    '../resource/ailinggo-unown-service_account.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
gc1 = gc.open("python-linkage-sample").worksheet('시트1')
gc1.update_acell('B2', 'novels')
gc2 = gc1.get_all_values()
print(gc2)
#
# gc = gspread.authorize(credentials)
# # gc.del_spreadsheet("1PTAMMwtyAmeLm3OoPLsCqTmovNg8MHVAIW23uQcrHuk")
# gs = gc.create("test.xls", folder_id='1dKWXYdqpJJ0AwOiDmcVJF48TvxWApYEF')
# worksheet = gs.add_worksheet(title='시트1', rows='1', cols='1')
# gs.share('test.ailinggo@gmail.com', perm_type='user', role='writer')
# # sh = gc.open("python-linkage-sample")