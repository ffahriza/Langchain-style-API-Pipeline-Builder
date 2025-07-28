import json

from .registry import get_module  # jika dalam satu package

class Pipeline:
    def __init__(self, config: dict):
        self.steps = []
        for step in config["pipeline"]:
            module_cls = get_module(step["type"])
            instance = module_cls(step.get("config", {}))
            self.steps.append((step["name"], instance))

    def run(self, input_data):
        data = input_data
        for name, module in self.steps:
            data = module.run(data)
        return data
