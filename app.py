import base64
import os
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from sendgrid import SendGridAPIClient


SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
FROM_EMAIL = 'BISV.Book.Exchange.Club@gmail.com'

def send_email(to_email, subject, html_content):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
        print('Sent Email To: ' + to_email)
    except Exception as e:
        print('send_email Exception: ' + str(e))


def send_email(to_email, subject, html_content, file_path, file_name):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        html_content=html_content)
    #file_path = '/Users/clin/Downloads/tenline.csv'
    #file_name = 'tenline.csv'

    try:
        data = None
        with open(file_path, 'rb') as f:
            data = f.read()
            f.close()
        if (data is not None):
            encoded = base64.b64encode(data).decode()
            attachment = Attachment()
            attachment.file_content = FileContent(encoded)
            attachment.file_type = FileType('text/csv')
            attachment.file_name = FileName(file_name)
            attachment.disposition = Disposition('attachment')
            attachment.content_id = ContentId('Example Content ID')
            message.attachment = attachment

            sendgrid_client = SendGridAPIClient(SENDGRID_API_KEY)
            response = sendgrid_client.send(message)
            print('Sent Email To: ' + to_email + ' with attachment: ' + file_path)
            #print(response.status_code)
            #print(response.body)
            #print(response.headers)
    except Exception as e:
        print('send_email Exception: ' + str(e))
