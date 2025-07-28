# 🧠 AI Pipeline Builder

A simple, modular pipeline builder for AI tasks such as summarization, sentiment analysis, and more — all configurable via YAML and runnable through a GUI with Streamlit.

---

## 📦 Features

- 🧩 Modular design (easily extendable with custom modules)
- 🔄 YAML-based pipeline configuration
- 💬 Supports summarization and sentiment analysis out-of-the-box
- 🌐 Web-based interface using Streamlit
- 🔍 Explainability layer and result visualization
- 🗂️ Preset loader and registry system for your custom components

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai_pipeline_builder.git
cd ai_pipeline_builder
```
### Install dependencies
```bash
pip install -r requirements.txt
```

### Runt the Steamlit app
```
streamlit run gui/runner.py #It will launch a web interface at: http://localhost:8502
```

### Project Structure
```bash
ai_pipeline_builder/
├── builder/
│   ├── modules/           # Custom AI modules (summarizer, sentiment, etc.)
│   ├── pipeline.py        # Pipeline runner
│   ├── validator.py       # YAML config validator
│   └── registry.py        # Component registry
│
├── gui/
│   ├── runner.py          # Streamlit UI to run pipeline
│   ├── app.py             # (Optional) extended GUI
│   └── builder.py         # GUI helper
│
├── config/
│   └── sample_pipeline.yaml
│
├── test/                  # Unit tests
├── utils/                 # Helper utilities
├── dag_visualizer.py      # Visualize pipeline as a graph
├── save_preset.py         # Save pipeline presets
└── requirements.txt
```

### Example
```
pipeline:
  - module: summarizer
  - module: sentiment
```

### Custom Module Integration
To add your own module, create a Python file in builder/modules/:
```
def run(input_text, config=None):
    return f"Processed: {input_text}" #Register it in registry.py.
```
📄 License
MIT © 2025 Andra


