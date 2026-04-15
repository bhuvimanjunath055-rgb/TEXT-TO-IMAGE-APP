import streamlit as st
import requests
from PIL import Image
import io

st.title("Text to Image Generator")

# 🔑 Paste your token here
API_TOKEN = "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"

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response

prompt = st.text_input("Enter prompt")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating..."):
            res = query(prompt)

            if res.status_code == 200:
                image = Image.open(io.BytesIO(res.content))
                st.image(image)
            else:
                st.error(res.text)
    else:
        st.warning("Enter prompt")
