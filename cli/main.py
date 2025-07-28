import argparse
import yaml
from builder.pipeline import Pipeline
from builder.validator import validate_config

parser = argparse.ArgumentParser(description="Run AI Pipeline from config")
parser.add_argument("--config", required=True, help="Path to YAML config")
parser.add_argument("--input", required=True, help="Text input")

args = parser.parse_args()

with open(args.config, 'r') as file:
    config = yaml.safe_load(file)

validate_config(config)

pipeline = Pipeline(config)
result = pipeline.run(args.input)
print("Pipeline Output:", result)
