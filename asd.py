import streamlit as st
import streamlit.components.v1 as components

# Read the HTML file
with open("macedonian_nihss_calculator.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display the app title
st.title("NIHSS Калкулатор")

# Display the HTML content
components.html(html_content, height=900)