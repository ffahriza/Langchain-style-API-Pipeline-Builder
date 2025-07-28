from builder.registry import register_module

@register_module("summarizer")
class Summarizer:
    def __init__(self, config):
        self.max_length = config.get("max_length", 100)

    def run(self, input_text):
        # Dummy summarization logic
        return input_text[:self.max_length]
