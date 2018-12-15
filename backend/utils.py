import traceback
import logging
from models import Log

class DBLogger(logging.Handler):
    def emit(self, record):
        trace =""
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc().replace("\n"," ")
        log = Log.create(
                logger=record.__dict__['name'],
                level=record.__dict__['levelname'],
                trace=trace,
                msg=record.__dict__['msg']
        )
