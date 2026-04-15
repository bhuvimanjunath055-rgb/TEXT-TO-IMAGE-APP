import streamlit as st
import requests

st.title("🎨 Text to Image Generator")

# 👉 Paste your Hugging Face token here
API_TOKEN = "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"

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def generate_image(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

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
            image, error = generate_image(prompt)

            if error:
                if "loading" in str(error).lower():
                    st.warning("Model loading... wait 20 seconds and click again")
                else:
                    st.error(error)
            else:
                st.image(image)
                st.success("Done ✅")
