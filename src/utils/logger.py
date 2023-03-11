import logging


# logger = logging.Logger()

def get_logger():
    console = logging.StreamHandler()
    logger = logging.getLogger()
    logger.propagate = False
    logger.addHandler(console)
    logger.setLevel(logging.INFO)
    return logger
