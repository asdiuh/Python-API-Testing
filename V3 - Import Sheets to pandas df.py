from Google import Create_Service  
import pandas as pd

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gsheetId = '1jAuWMUY-1vkt2jFPje3LHVnmTn1MDPLw58HZu72aCbM'

s = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
gs = s.spreadsheets()
rows = gs.values().get(spreadsheetId = gsheetId, range = 'Sheet2').execute()
data = rows.get('values')
df = pd.DataFrame(data)
print(df)
pd.DataFrame.to_csv(df, 'V3 - Import Sheets to pandas df.csv')