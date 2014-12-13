__author__ = 'Jonas Eberle <jonas.eberle@eberle-mail.de>'

import logging
import sys

LOGGER = logging.getLogger(__name__)

DEBUG_MSG_FORMAT = '[%(asctime)s] [%(levelname)s] file=%(pathname)s \
line=%(lineno)s module=%(module)s function=%(funcName)s msg=%(message)s'

ERROR_MSG_FORMAT = DEBUG_MSG_FORMAT

INFO_MSG_FORMAT = '[%(asctime)s] Message: %(message)s'

TIME_FORMAT = '%a, %d %b %Y %H:%M:%S'

LOGLEVELS = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'NOTSET': logging.NOTSET,
}

LOGFORMATS = {
    'CRITICAL': ERROR_MSG_FORMAT,
    'ERROR': ERROR_MSG_FORMAT,
    'WARNING': DEBUG_MSG_FORMAT,
    'INFO': INFO_MSG_FORMAT,
    'DEBUG': DEBUG_MSG_FORMAT,
    'NOTSET': '%(message)s',
}

def setup_logger(config=None):
    """Initialize logging facility"""

    logfile = None
    loglevel = 'DEBUG'

    if config != None:
        if 'logfile' in config: logfile = config['logfile']
        if 'loglevel' in config: loglevel = config['loglevel']
    if loglevel not in LOGLEVELS:
        raise RuntimeError('Given loglevel is not valid!')

    # Setup logging globally (not only for the pycsw module)
    # based on the parameters passed.
    logformat = LOGFORMATS[loglevel]

    if logfile != None:
        hdlr = logging.StreamHandler(sys.stdout)
        hdlr.setFormatter(logging.Formatter(logformat))
        hdlr.setLevel(logging.INFO)
        LOGGER.addHandler(hdlr)

    logging.basicConfig(level=LOGLEVELS[loglevel],
                        filename=logfile,
                        datefmt=TIME_FORMAT,
                        format=logformat)

    LOGGER.info('Logging initialized (level: %s).' % loglevel)
    LOGGER.debug('Debug')


class MyFormatter(logging.Formatter):

    err_fmt  = "ERROR: %(msg)s"
    dbg_fmt  = '%(asctime)s] [%(levelname)s] file=%(pathname)s line=%(lineno)s module=%(module)s function=%(funcName)s msg=%(message)s'
    info_fmt = "Message: %(msg)s"


    def __init__(self, fmt="%(levelno)s: %(msg)s"):
        logging.Formatter.__init__(self, fmt)


    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == logging.DEBUG:
            self._fmt = MyFormatter.dbg_fmt

        elif record.levelno == logging.INFO:
            self._fmt = MyFormatter.info_fmt

        elif record.levelno == logging.ERROR:
            self._fmt = MyFormatter.err_fmt

        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)

        # Restore the original format configured by the user
        self._fmt = format_orig

        return result