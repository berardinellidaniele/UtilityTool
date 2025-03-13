import logging
import os

def get_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(os.path.join("logs", "filemanager.log")),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger()
