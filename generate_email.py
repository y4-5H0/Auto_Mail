import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Prompt Gemini to generate an email based on the provided template and recipient's email.
def generate_email_content(base_format, signature):
    prompt = f"""
    Based on the following format, generate a unique email with a new subject each time.
    keep the core motivation same. End with this signature: {signature}
    
    Format:
    {base_format}
    """
    
    # Initialize the Gemini model
    model = genai.GenerativeModel('gemini-pro')
    
    # Generate content
    response = model.generate_content(prompt)
    content = response.text
    return content
    