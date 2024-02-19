import streamlit as st

import pandas as pd
from PIL import Image

## AIzaSyA4ACANQRcchCNDXamY0Neyp9Yo_2dvK8w
#from google.generativeai import GenerativeModel
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
GOOGLE_API_KEY="AIzaSyA4ACANQRcchCNDXamY0Neyp9Yo_2dvK8w"
#api_key = os.getenv("AIzaSyA4ACANQRcchCNDXamY0Neyp9Yo_2dvK8w")
#GenerativeModel.configure(api_key=api_key)
genai.configure(api_key=GOOGLE_API_KEY)

model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input Image : ",key="input")
    
uploaded_file=st.file_uploader("Choose an image...",type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)
submit=st.button("Tell me about the image")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
