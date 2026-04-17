import streamlit as st
import requests
from PIL import Image
import io

st.title("Text to Image Generator")

# 🔐 Get API token from Streamlit Secrets
API_TOKEN = "your_huggingface_token"

# Hugging Face Model API
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Function to call API
def query(prompt):
    payload = {"inputs": prompt}
    
    response = requests.post(API_URL, headers=headers, json=payload)

    # Handle model loading (very common in deployment)
    if response.status_code == 503:
        return "⏳ Model is loading... Please try again in a few seconds."

    return response


# User input
prompt = st.text_input("Enter your prompt")

# Generate button
if st.button("Generate"):
    if prompt:
        with st.spinner("Generating image..."):
            result = query(prompt)

            # If model is loading
            if isinstance(result, str):
                st.warning(result)

            # Success case
            elif result.status_code == 200:
                try:
                    image = Image.open(io.BytesIO(result.content))
                    st.image(image, caption="Generated Image")
                except Exception as e:
                    st.error("Error displaying image")

            # Other errors
            else:
                st.error(f"Error {result.status_code}: {result.text}")
    else:
        st.warning("Please enter a prompt")
