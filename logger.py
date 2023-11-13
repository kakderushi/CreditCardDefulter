'''
logging is pratice of recording messages that provide
information about the status or behavoir or a program during excecution 
it's like taking notes about what your program is doing differnt point at time,
and it's immensly helpful for understanding and debugging code.
'''

import logging
from datetime import datetime
import os
# name of the file
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# join the path of current directoy path to log_path
Log_path=os.path.join(os.getcwd(),"logs")

os.makedirs(Log_path,exist_ok=True)

log_file_path=os.path.join(Log_path,LOG_FILE)
logging.basicConfig(level=logging.INFO,filename=log_file_path,format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")