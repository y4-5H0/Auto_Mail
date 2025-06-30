from mailer import send_email
from generate_email import generate_email
from utils import get_email_list

EMAIL_FILE = "data/recipients.xlsx"
SIGNATURE = "Best regards,\nYour Name"

with open("template/base_prompt.txt", "r") as file:
    base_format = file.read()
    
emails = get_email_list(EMAIL_FILE)

for recipient in emails:
    full_email = generate_email(base_format, SIGNATURE)
    subject_line = full_email.splitlines()[0]  # Assuming the first line is the subject
    body = '\n'.join(full_email.splitlines()[1:])  # The rest is the body
    send_email(recipient, subject_line, body)