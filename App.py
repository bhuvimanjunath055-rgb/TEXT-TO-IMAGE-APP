import streamlit as st
import requests
from PIL import Image
import io

st.title("🎨 Text to Image Generator")

# 👉 Paste your Hugging Face token here
API_TOKEN = "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"

# Correct API URL
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def generate_image(prompt):
    payload = {"inputs": prompt}
    
    response = requests.post(API_URL, headers=headers, json=payload)

    # If error comes
    if response.status_code != 200:
        try:
            return None, response.json()
        except:
            return None, {"error": response.text}

    return response.content, None

prompt = st.text_input("Enter your prompt")

if st.button("Generate Image"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating image..."):
            image_bytes, error = generate_image(prompt)

            if error:
                st.error(error)
            else:
                try:
                    image = Image.open(io.BytesIO(image_bytes))
                    st.image(image, caption="Generated Image")
                    st.success("Done ✅")
                except:
                    st.error("Image not generated. Try again after few seconds.")
