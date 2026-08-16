import logging

def setup_logger():
    logger = logging.getLogger("NetmapperZ")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%H:%M:%S')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
    return logger

def get_logger():
    return logging.getLogger("NetmapperZ")
