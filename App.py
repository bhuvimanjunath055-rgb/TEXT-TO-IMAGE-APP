import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

headers = {"Authorization": "Bearer YOUR_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

st.title("Text to Image Generator")

prompt = st.text_input("Enter your prompt")

if st.button("Generate Image"):
    if prompt:
        image_bytes = query({"inputs": prompt})
        st.image(image_bytes)
    else:
        st.warning("Enter a prompt")
