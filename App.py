import streamlit as st
from huggingface_hub import InferenceClient

st.title("Text to Image Generator")

client = InferenceClient(
    model="stabilityai/stable-diffusion-xl-base-1.0",
    token="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"
)

prompt = st.text_input("Enter your prompt")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating image..."):
            try:
                image = client.text_to_image(prompt)
                st.image(image)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Enter a prompt")
