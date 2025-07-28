import streamlit as st
import yaml

AVAILABLE_MODULES = {
    "summarizer": {"max_length": 100},
    "sentiment": {},
    "rewriter": {"style": "formal"}
}

st.title("🧩 AI Pipeline Builder")

st.markdown("### ➕ Tambahkan Step ke Pipeline")
pipeline = []

step_count = st.number_input("Berapa banyak step?", min_value=1, max_value=10, value=2)
for i in range(step_count):
    st.markdown(f"#### Step {i+1}")
    step_name = st.text_input(f"Nama Step {i+1}", key=f"name_{i}")
    module_type = st.selectbox(f"Module Type", list(AVAILABLE_MODULES.keys()), key=f"type_{i}")
    
    config = {}
    for k, v in AVAILABLE_MODULES[module_type].items():
        config_value = st.text_input(f"{module_type} config - {k}", str(v), key=f"cfg_{i}_{k}")
        config[k] = config_value

    pipeline.append({
        "name": step_name,
        "type": module_type,
        "config": config
    })

if st.button("💾 Export to YAML"):
    config_dict = {"pipeline": pipeline}
    st.code(yaml.dump(config_dict), language="yaml")
    st.download_button("Download YAML", yaml.dump(config_dict), file_name="pipeline.yaml")

