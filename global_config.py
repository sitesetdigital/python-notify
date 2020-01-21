global_config = None

if global_config is None:
    from .config import Config
    global_config = Config()