import streamlit as st
import requests
from PIL import Image
import io

st.title("🎨 Text to Image Generator")

# 🔑 Paste your sir's Hugging Face token here
API_TOKEN = "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"

# ✅ Stable working model
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_image(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code != 200:
        return None, response.text

    return response.content, None

prompt = st.text_input("Enter your prompt")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            image_bytes, error = generate_image(prompt)

            if error:
                st.error(error)
            else:
                try:
                    image = Image.open(io.BytesIO(image_bytes))
                    st.image(image)
                    st.success("Image generated ✅")
                except:
                    st.warning("Model loading... wait 20–30 seconds and try again")
    else:
        st.warning("Please enter a prompt")
