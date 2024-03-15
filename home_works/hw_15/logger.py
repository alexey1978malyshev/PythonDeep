import logging


def log(text, logfile):
    f = '{levelname:<8} - {asctime} | {msg}'
    logging.basicConfig(level=logging.INFO, filename=logfile, filemode='a+', format=f, style='{')
    logger = logging.getLogger(__name__)
    logger.info(text)