# Language-Translation

import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Streamlit app
st.title("Simple Language Translator")

# Input text
input_text = st.text_area("Enter text to translate:")

# Language selection
src_lang = st.selectbox("Select source language:", ["en", "es", "fr", "de", "zh-cn"])
dest_lang = st.selectbox("Select target language:", ["en", "es", "fr", "de", "zh-cn"])

# Translate button
if st.button("Translate"):
    if input_text:
        # Perform translation
        translated_text = translator.translate(input_text, src=src_lang, dest=dest_lang).text
        st.write("Translated Text:")
        st.write(translated_text)
    else:
        st.write("Please enter some text to translate.")
