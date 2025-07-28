from builder.registry import register_module

@register_module("sentiment")
class SentimentAnalyzer:
    def __init__(self, config):
        pass

    def run(self, input_text):
        if "good" in input_text.lower():
            return "Positive"
        elif "bad" in input_text.lower():
            return "Negative"
        return "Neutral"
