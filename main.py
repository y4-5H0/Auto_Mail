import time
from mailer import send_email
from generate_email import generate_email_content
from utils import get_email_list
from config import EMAIL_DELAY

EMAIL_FILE = "data/recipients.xlsx"
SIGNATURE = "Best regards,\nYour Name"

with open("templates/base_prompt.txt", "r") as file:
    base_format = file.read()
    
emails = get_email_list(EMAIL_FILE)

for i, recipient in enumerate(emails, 1):
    full_email = generate_email_content(base_format, SIGNATURE)
    subject_line = full_email.splitlines()[0]  # Assuming the first line is the subject
    body = '\n'.join(full_email.splitlines()[1:])  # The rest is the body
    send_email(recipient, subject_line, body)
    
    print(f"[{i}] Sent to {recipient}. Waiting for {EMAIL_DELAY} seconds before sending the next email.")
    time.sleep(EMAIL_DELAY)  # Wait before sending the next email