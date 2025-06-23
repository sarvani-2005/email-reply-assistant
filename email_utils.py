# email_utils.py

import os
import base64
import pickle
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def gmail_authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

def get_latest_email(service):
    result = service.users().messages().list(userId='me', maxResults=1, labelIds=['INBOX'], q="is:unread").execute()
    messages = result.get('messages', [])

    if not messages:
        return None, None

    msg = service.users().messages().get(userId='me', id=messages[0]['id'], format='full').execute()
    headers = msg['payload']['headers']
    sender = next(header['value'] for header in headers if header['name'] == 'From')
    parts = msg['payload'].get('parts', [])

    for part in parts:
        if part['mimeType'] == 'text/plain':
            data = part['body']['data']
            text = base64.urlsafe_b64decode(data).decode()
            return sender, text

    return sender, "No readable text found."

def send_reply(service, to, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = 'Re: Your Email'
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw}
    message = service.users().messages().send(userId='me', body=body).execute()
    return message
