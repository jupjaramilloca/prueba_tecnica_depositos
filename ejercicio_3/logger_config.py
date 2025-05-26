import logging
import os
import json

def setup_logger(config_path="config.json", level=logging.INFO):
    # Leer config
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    log_dir = config.get("log_dir", "logs")
    log_file = config.get("log_file", "app.log")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    logger = logging.getLogger("ProyectoLogger")
    logger.setLevel(level)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    
    fh = logging.FileHandler(os.path.join(log_dir, log_file), encoding="utf-8")
    fh.setLevel(level)
    fh.setFormatter(formatter)
    
    if not logger.hasHandlers():
        logger.addHandler(ch)
        logger.addHandler(fh)
    
    return logger
