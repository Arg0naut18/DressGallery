import logging
from src.constants import LoggerConstants


class GalleryLogger:
    def __init__(self) -> None:
        logging.basicConfig(filename=LoggerConstants.FILENAME,
                            format=LoggerConstants.FORMAT,
                            filemode='w')
        self.logger = logging.getLogger()
        self.logger.setLevel(LoggerConstants.LOG_LEVEL)


logger = GalleryLogger().logger
