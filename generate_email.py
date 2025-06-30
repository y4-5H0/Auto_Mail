import pandas as pd
import openai
from config import OPENAI_API_KEY

# Use pands to read the Excel file and extract emails.
def generate_email(file_path):
    df = pd.read_excel(file_path)
    return df['Email'].dropna().tolist()

#Prompt ChatGPT to generate an email based on the provided template and recipient's email.

def generate_email_content(base_format, signature):
    prompt = f"""
    Based on the following format, generate a unique email with a new subject each time.
    keep the core motivation same. End with this signature: {signature}
    
    Format:
    {base_format}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4"
        messages=[{"role": "user", "content": prompt},]
        temperature=0.9
    )
    content = response['choices'][0]['message']['content']
    return content
    