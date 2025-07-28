# utils/save_preset.py
import json

def export_pipeline_config(config, filename):
    with open(filename, 'w') as f:
        json.dump(config, f, indent=2)

def load_pipeline_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)
