import os
import logging
from datetime import datetime

LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOGS_PATH,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE_PATH,
    format=LOG_FMT)
