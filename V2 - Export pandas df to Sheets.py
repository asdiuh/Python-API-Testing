from Google import Create_Service
import pandas as pd
import numpy as np

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gsheetId = '1jAuWMUY-1vkt2jFPje3LHVnmTn1MDPLw58HZu72aCbM'

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

def clear_sheets(sheet_delete):
    #range ='{}!A1:Z1000'.format(sheet_delete)
    request = service.spreadsheets().values().clear(
    spreadsheetId=gsheetId,
    #range='Sheet1!A1:Z1000',
    range = '{}!A:ZZ'.format(sheet_delete),
    body = {})
    response = request.execute()

def Export_Data_To_Sheets2():
    URL = r'https://files.digital.nhs.uk/publicationimport/pub20xxx/pub20188/ccg-pres-data-oct-dec-2015-un-dat.csv'
    df = pd.read_csv(URL)
    df.replace(np.nan, '', inplace=True)

    print("appending first workbook")
    response_date = service.spreadsheets().values().append(
        spreadsheetId=gsheetId,
        valueInputOption='RAW',
        range='Sheet2!A1',
        body=dict(
            majorDimension='ROWS',
            values=df.T.reset_index().T.values.tolist())
            #      df.T.reset_index().T.values.tolist()
    ).execute()

def Export_Data_To_Sheets3():
    URL2 = r'https://raw.githubusercontent.com/franciscadias/data/master/kc_house_data.csv'
    df2 = pd.read_csv(URL2)
    df2.replace(np.nan, '', inplace=True)

    print("appending second workbook")
    response_date = service.spreadsheets().values().append(
        spreadsheetId=gsheetId,
        valueInputOption='RAW',
        range='Sheet3!A1',
        body=dict(
            majorDimension='ROWS',
            values=df2.T.reset_index().T.values.tolist())
    ).execute()

def Export_Data_To_Sheets4():
    print("appending third workbook")
    list = [["valuea1"], ["valuea2"], ["valuea3"]]
    resource = {
        "majorDimension": "COLUMNS",
        "values": list
    }
    
    response_date = service.spreadsheets().values().append(
        spreadsheetId=gsheetId,
        range='Sheet4!A1',
        body=resource,
        valueInputOption="RAW"
    ).execute()

print("clearing sheet 1")
#clear_sheets('Sheet1')
print("clearing sheet 2")
#clear_sheets('Sheet2')
print("clearing sheet 3")
#clear_sheets('Sheet3')
print("clearing sheet 4")
#clear_sheets('Sheet4')
#Export_Data_To_Sheets2()
#Export_Data_To_Sheets3()
Export_Data_To_Sheets4()
print("Finished")