from datetime import datetime

def on_config(config, **kwargs):
    config.copyright = f"Copyright © 2024 - {datetime.now().year} PyGreece"
    return config
