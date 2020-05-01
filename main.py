"""Use to delete format markdown checkbox."""
from dotenv import load_dotenv
import json
import os
from os.path import join, dirname
import requests

def format_textfile(txtfile):
    """
    Read txtfile and send function for format
    """
    text = txtfile.read()
    translate_checkbox_to_bullet(text)

def translate_checkbox_to_bullet(text):
    """
    Delete checkbox of markdown into bullet(-)
    """
    replaced_text = text.replace('[ ]', '').replace('[x]', '')
    output_txt_file(replaced_text)

def output_txt_file(text):
    """
    Output formatted text to console and src/formatted_text.txt
    """
    with open('src/formatted_text.txt', mode='w') as format_text:
        format_text.write(text)
        print('Complete. Please check src/formatted_text.txt')
        print('-----------------------------------------------')
        print(text)
        print('-----------------------------------------------')
    send_slack_notification(text)

def send_slack_notification(formated_text):
    """
    Send notification to Slack with text.
    """
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    webhook = os.environ.get("INCOMING_WEBHOOK")
    channel = os.environ.get("CHANNEL")
    user_name = os.environ.get("USER_NAME")
    user_mention = os.environ.get("USER_MENTION")
    text = f"今日の{user_name}のToDoです。よろしくお願いします。"

    attachments =  [{
        'author_name': f"<@{user_mention}>",
        'text': formated_text,
        'color': '#2eb886'
    }]

    data=json.dumps({
        "text": text,
        "channel": channel,
        "attachments": attachments
    })
    r = requests.post(webhook, data=data)
    print(r)
    print(r.text)

print('Start to convert...')
f = open('src/text.txt')
format_textfile(f)
f.close()
