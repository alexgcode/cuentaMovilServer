import logging
import math

LOG_FORMAT = "%(levelname)s(%(name)s) %(asctime)s - %(message)s" # format string
logging.basicConfig(filename="D:\\Projects on github\\cuentaMovil\\test.Log", level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()    # nombre por defecto del logger = root

