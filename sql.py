import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()  # load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey, act like a skilled or very experienced Database Administrator 
with a deep understanding of the tech field, SQL, MYSQL, DB2, software engineering, data science, data analysis, and big data engineering.
Your task is to evaluate the SQL code and queries.
You must consider that SQL is very important, and you should provide 
the best assistance for improving the SQL queries.
Analyse the entire code as a whole always and give the respone in output for the entire improved code.
Look for code optimsiation oppurtunuties and restructure the entire code and generate the output

I want the response as an improved version of the input , always structured like a professional coder.
"""

# Streamlit app
st.title("DB2 SQL ANALYZER")
st.text("Improve Your SQL")
jd = st.text_area("Paste the SQL or any code")

# Commented out file uploader part
# uploaded_file = st.file_uploader("Upload Your Code/Query", type="pdf", help="Please upload the pdf")

submit = st.button("Run Analyzer")

if submit:
    # if uploaded_file is not None:
    #     text = input_pdf_text(uploaded_file)
    response = get_gemini_response(input_prompt.format(jd=jd))
    st.subheader(response)
