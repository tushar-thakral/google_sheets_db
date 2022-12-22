from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pandas import DataFrame


def insert_data(request):

    # Retrieving the data to be inserted from the request
    u_name = request.POST.get('user_name')
    u_contact = request.POST.get('user_contact')

    scope = ['https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name("gs_credentials.json", scope)
    client = gspread.authorize(credentials)

    # Create a blank spreadsheet
    # sheet = client.create("NewDatabase")

    sh = client.open("NewDatabase")

    # Insert your gmail id in your_gmail_id below and uncomment to share the sheet with yourself
    sh.share('tushar.thakral@gmail.com', perm_type='user', role='writer')

    # DataFrame with the data to be inserted
    df = DataFrame({'Name': u_name, 'Contact Number': u_contact}, index=[0])
    values = df.values.tolist()

    # Appending the data to the sheet
    sh.values_append('Sheet1', {'valueInputOption': 'RAW'}, {'values': values})

    return render(request, "my_app/user_details.html", {})