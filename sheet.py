import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("jobs.json", scope)

client = gspread.authorize(creds)

sheet = client.open("jobs").sheet1

def insert(info):
    row = info
    sheet.insert_row(row, 2)