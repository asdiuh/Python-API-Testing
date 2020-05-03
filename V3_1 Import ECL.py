import os
os.chdir('/home/redhwanzaman1989/Python API Test/')

from Google import Create_Service
import pandas as pd


CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
GSheetId = '1Ro7c8jUDUoDAvchOZd-jhjJ-1BHGAkDLFc-at2KXE0k'
#Create_Service(client_secret_file, api_name, api_version, *scopes)

s = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
gs = s.spreadsheets()
rows = gs.values().get(spreadsheetId = GSheetId, range = 'NewData1').execute()
data = rows.get('values')
ColumnNames = data[0]
data1 = data[1:len(data)]
df = pd.DataFrame(data1, columns = ColumnNames)
pd.DataFrame.to_csv(df, 'V3 - ECL.csv', index = False)