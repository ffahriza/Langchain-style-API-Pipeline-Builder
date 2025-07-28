import streamlit as st
import yaml
from builder.pipeline import Pipeline
from builder.validator import validate_config

st.title("🚀 Run Your AI Pipeline")

uploaded_config = st.file_uploader("Upload YAML Pipeline Config", type=["yaml", "yml"])
input_text = st.text_area("Input Text")

if uploaded_config and input_text:
    config = yaml.safe_load(uploaded_config)
    try:
        validate_config(config)
        pipeline = Pipeline(config)
        result = pipeline.run(input_text)
        st.success("Pipeline Output:")
        st.write(result)
    except Exception as e:
        st.error(f"Error: {e}")
