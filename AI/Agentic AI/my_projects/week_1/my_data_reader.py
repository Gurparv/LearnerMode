# Reading Pdf data

from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

def reading_data():
    load_dotenv(override=True)
    reader = PdfReader("my_profile.pdf")
    number_of_pages = len(reader.pages)
    content = ""
    for i in range(number_of_pages):
        page = reader.pages[i]
        content += page.extract_text()
    my_email = os.getenv("MY_EMAIL") 
    #print(my_email)
    text = content.replace(my_email,"Oops! I forgot to share my email. You can connect with me on LinkedIn instead!")
    return text




