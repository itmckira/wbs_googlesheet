"""
Google Sheets Integration Module

This module provides functions to interact with Google Sheets API
for reading WBS items.
"""

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


def get_google_sheets_service():
    """
    Authenticate and return Google Sheets service.
    
    Returns:
        Google Sheets service object
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                raise FileNotFoundError(
                    "credentials.json not found. Please download it from Google Cloud Console."
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    try:
        service = build('sheets', 'v4', credentials=creds)
        return service
    except HttpError as err:
        print(f"An error occurred: {err}")
        raise


def read_sheet_data(spreadsheet_id, range_name):
    """
    Read data from a Google Sheet.
    
    Args:
        spreadsheet_id: The ID of the spreadsheet
        range_name: The A1 notation of the range to retrieve
    
    Returns:
        List of rows from the sheet
    """
    service = get_google_sheets_service()
    
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        
        values = result.get('values', [])
        return values
    
    except HttpError as err:
        print(f"An error occurred: {err}")
        raise


def get_spreadsheet_info(spreadsheet_id):
    """
    Get basic information about a spreadsheet.
    
    Args:
        spreadsheet_id: The ID of the spreadsheet
    
    Returns:
        Dictionary with spreadsheet information
    """
    service = get_google_sheets_service()
    
    try:
        sheet = service.spreadsheets()
        result = sheet.get(spreadsheetId=spreadsheet_id).execute()
        
        return {
            'title': result.get('properties', {}).get('title'),
            'sheets': [s.get('properties', {}).get('title') 
                      for s in result.get('sheets', [])]
        }
    
    except HttpError as err:
        print(f"An error occurred: {err}")
        raise
