# gui/app.py
import streamlit as st
from builder.pipeline import Pipeline

uploaded_config = st.file_uploader("Upload Pipeline YAML")

if uploaded_config:
    import yaml
    config = yaml.safe_load(uploaded_config)
    pipeline = Pipeline(config)
    input_text = st.text_area("Input Text")
    if st.button("Run Pipeline"):
        result = pipeline.run(input_text)
        st.write(result)
