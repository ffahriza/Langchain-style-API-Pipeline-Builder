MODULE_REGISTRY = {}

def register_module(name):
    def wrapper(cls):
        MODULE_REGISTRY[name] = cls
        return cls
    return wrapper

def get_module(name):
    return MODULE_REGISTRY[name]
