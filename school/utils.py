
from email.header import decode_header

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth

from django.shortcuts import render
from django.http import JsonResponse

def send_sms(recipient, sms_message):

    url = "https://apisms.beem.africa/v1/send"
    

    data = {
        "source_addr": "INFO",
        "encoding": 0,
        "message": 'SBMS  \n\n'+ sms_message,
        "recipients": [
            {
                "recipient_id": 1,
                "dest_addr": recipient
            },
            
        ]
    }

    username = settings.BEEM_AFRICA_API_KEY
    password = sender_id = settings.BEEM_AFRICA_SENDER_ID

    response = requests.post(url, json=data, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        print("SMS sent successfully!")
    else:
        print("SMS sending failed. Status code:", response.status_code)
        print("Response:", response.text)
        
       
