import streamlit as st
from huggingface_hub import InferenceClient

st.title("Text to Image Generator")

# Create client
client = InferenceClient(
    model="stabilityai/stable-diffusion-2",
    token="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"
)

prompt = st.text_input("Enter your prompt")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating image..."):
            try:
                image = client.text_to_image(prompt)
                st.image(image, caption="Generated Image")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a prompt")
