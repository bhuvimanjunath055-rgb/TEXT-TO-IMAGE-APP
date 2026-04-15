import streamlit as st
import requests
from PIL import Image
import io

st.title("🎨 Text to Image Generator")

# ✅ Paste your Hugging Face token here
API_TOKEN = "hf_xxxxxxxxxxxxxxxxx"

# ✅ Correct working model
API_URL = "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"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_image(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    # If API gives error
    if response.status_code != 200:
        try:
            return None, response.json()
        except:
            return None, {"error": response.text}

    return response.content, None

prompt = st.text_input("Enter your prompt")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating... please wait"):
            image_bytes, error = generate_image(prompt)

            if error:
                st.error(error)
            else:
                try:
                    image = Image.open(io.BytesIO(image_bytes))
                    st.image(image)
                    st.success("Image generated ✅")
                except:
                    st.error("Model is loading... wait 20 seconds and try again")
    else:
        st.warning("Enter a prompt")
