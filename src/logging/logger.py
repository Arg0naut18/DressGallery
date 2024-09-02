from configs import LogConfig
from logging.config import dictConfig
import logging


class GalleryLogger:
    def __init__(self) -> None:
        self.logging_config = LogConfig.config
        dictConfig(self.logging_config)
        self.logger = logging.getLogger('gallery.logs')
