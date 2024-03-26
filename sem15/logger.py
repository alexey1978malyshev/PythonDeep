import logging


def log(level, message):
    log_format = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
                 'в строке {lineno:03d} функция "{funcName}()" ' \
                 'в {created} секунд записала сообщение: {msg}'
    logger = logging.getLogger(__name__)
    levels = {'debug': logger.debug,
              'info': logger.info,
              'warning': logger.warning,
              'error': logger.error,
              'critical': logger.critical}
    logging.basicConfig(level=logging.NOTSET, filename='log.txt', filemode='w', encoding='utf-8', format=log_format,
                        style='{')
    levels[level](message)